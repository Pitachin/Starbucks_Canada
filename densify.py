# Path B: Data-driven gap-filling (with resume + checkpoint).
# Fix: truncation detection is self-contained here, so Stage 3 scraping
# does NOT pollute the truncation log.
import pandas as pd
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from scraper import get_store_locs
from city import make_grid
import config

GAP_PROVINCES = ["ON", "AB", "BC"]
TRUNCATED_FILE = "truncated_clean.json"   # clean detected points (not the polluted .txt)
CHECKPOINT = "scrape_progress.json"


def get_gap_province_coords():
    """Load postal coords, keep only the gap provinces (ON/AB/BC)."""
    zips = pd.read_csv(config.INPUT_COORDS)
    zips = zips[zips["province-code"].isin(GAP_PROVINCES)]
    zips = zips[["latitude", "longitude"]].drop_duplicates()
    coords = list(zip(zips["latitude"], zips["longitude"]))
    print(f"Gap-province postal coords: {len(coords)}")
    return coords


def detect_truncation(coords, save_every=50):
    """Scrape postal coords and return those returning >= 50 stores (truncated).
    Self-contained — does NOT rely on scraper's logging, so no pollution."""
    truncated = []
    total = len(coords)

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(get_store_locs, c): c for c in coords}
        done = 0
        for future in as_completed(futures):
            coord = futures[future]
            stores = future.result()
            if len(stores) >= 50:                 # truncated
                truncated.append(coord)
            done += 1
            if done % save_every == 0:
                print(f"{done}/{total} checked, {len(truncated)} truncated")

    print(f"Total truncated coords: {len(truncated)}")
    # Save clean detected points
    with open(TRUNCATED_FILE, "w") as f:
        json.dump([list(c) for c in truncated], f)
    return truncated


def load_truncated_coords():
    """Load previously detected truncated coords from the clean JSON file."""
    if not os.path.exists(TRUNCATED_FILE):
        return None
    with open(TRUNCATED_FILE) as f:
        coords = [tuple(c) for c in json.load(f)]
    print(f"Loaded {len(coords)} truncated coords from {TRUNCATED_FILE}")
    return coords


def densify_around(truncated_coords, radius=0.05, step=0.03):
    """Generate a dense grid around each truncated coordinate."""
    extra = []
    for coord in truncated_coords:
        extra += make_grid(coord[0], coord[1], radius=radius, step=step)
    extra = list(set(extra))   # dedupe
    print(f"Densified coords generated: {len(extra)}")
    return extra


def scrape_with_resume(coords, save_every=100):
    """Scrape with checkpoint — resumes after interruption."""
    done_coords = set()
    all_stores = []

    if os.path.exists(CHECKPOINT):
        with open(CHECKPOINT) as f:
            data = json.load(f)
            done_coords = set(tuple(c) for c in data["done"])
            all_stores = data["stores"]
        print(f"Resumed: {len(done_coords)} done, {len(all_stores)} stores so far")

    todo = [c for c in coords if tuple(c) not in done_coords]
    print(f"Remaining: {len(todo)} / {len(coords)}")

    def save_checkpoint():
        with open(CHECKPOINT, "w") as f:
            json.dump({"done": [list(c) for c in done_coords],
                       "stores": all_stores}, f)

    count = 0
    try:
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(get_store_locs, c): c for c in todo}
            for future in as_completed(futures):
                coord = futures[future]
                all_stores += future.result()
                done_coords.add(tuple(coord))
                count += 1
                print(f"{count} / {len(todo)}")
                if count % save_every == 0:
                    save_checkpoint()
                    print(f"  checkpoint saved ({len(all_stores)} stores)")
    finally:
        save_checkpoint()
        print(f"  final checkpoint saved ({len(all_stores)} stores)")

    return all_stores


def main():
    # --- Stage 1: detect truncation (reuse if already detected) ---
    print("=== Stage 1: detecting truncation in ON/AB/BC ===")
    truncated = load_truncated_coords()
    if truncated is None:                          # not detected yet → detect now
        gap_coords = get_gap_province_coords()
        truncated = detect_truncation(gap_coords)

    if not truncated:
        print("Nothing truncated. Data may already be complete.")
        return

    # --- Stage 2: densify around truncated points ---
    print("\n=== Stage 2: densifying around truncated points ===")
    extra_coords = densify_around(truncated)

    # --- Stage 3: scrape densified points (RESUMABLE) ---
    print("\n=== Stage 3: scraping densified points ===")
    new_stores = scrape_with_resume(extra_coords)
    new_df = pd.DataFrame(new_stores)

    # --- Stage 4: merge into existing data ---
    print("\n=== Stage 4: merging with existing data ===")
    if not os.path.exists(config.STORES_CSV):
        print(f"⚠️ {config.STORES_CSV} not found. Saving densify result separately.")
        new_df["store_id"] = new_df["store_id"].astype(str)
        new_df = new_df.drop_duplicates(subset="store_id").reset_index(drop=True)
        new_df = new_df[new_df["country"] == "CA"].reset_index(drop=True)
        new_df.to_csv("densify_result.csv", index=False, encoding="utf-8-sig")
        print(f"Saved {len(new_df)} stores to densify_result.csv")
        return

    existing = pd.read_csv(config.STORES_CSV)
    combined = pd.concat([existing, new_df], ignore_index=True)
    # 🔑 FIX: unify store_id type before dedup.
    # API returns store_id as str, but read_csv infers it as int64.
    # Without this, concat makes the column 'object' (mixed int+str),
    # and drop_duplicates treats 1034072 (int) != "1034072" (str).
    combined["store_id"] = combined["store_id"].astype(str)

    combined = combined.drop_duplicates(subset="store_id").reset_index(drop=True)
    combined = combined[combined["country"] == "CA"].reset_index(drop=True)

    print(f"\nBefore: {len(existing)} stores")
    print(f"After:  {len(combined)} stores")
    print(combined["province_code"].value_counts())

    combined.to_csv(config.STORES_CSV, index=False, encoding="utf-8-sig")
    print(f"\nSaved {len(combined)} stores to {config.STORES_CSV}")

if __name__ == "__main__":
    main()