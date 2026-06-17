import requests
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
from record_time import timer
import config
from city import build_city_grids


def get_store_locs(coor: tuple, retries=5) -> list[dict]:
    """Fetch Starbucks stores near a given coordinate, with retry on failure."""
    params = {"lat": coor[0], "lng": coor[1]}

    for attempt in range(retries):
        try:
            response = requests.get(config.API_URL, params=params,
                                    headers=config.HEADERS, timeout=30)
        except requests.exceptions.RequestException as e:
            wait = 3 * (attempt + 1)
            print(f"Timeout {coor}, retry {attempt+1} in {wait}s")
            time.sleep(wait)
            continue                          # retry

        time.sleep(random.uniform(1, 1.5))

        if response.status_code == 200:
            stores = []
            for item in response.json():
                s = item["store"]
                stores.append({
                    "store_id": s.get("id"),
                    "name": s.get("name"),
                    "city": s.get("address", {}).get("city"),
                    "province_code": s.get("address", {}).get("countrySubdivisionCode"),
                    "postal_code": s.get("address", {}).get("postalCode"),
                    "country": s.get("address", {}).get("countryCode"),
                    "latitude": s.get("coordinates", {}).get("latitude"),
                    "longitude": s.get("coordinates", {}).get("longitude"),
                    "ownership": s.get("ownershipTypeCode"),
                    "amenities": [a["name"] for a in s.get("amenities", [])],
                    "schedule": s.get("schedule"),
                })
            
            return stores
        elif response.status_code in (500, 429, 503):   # server err → retry
            wait = 3 * (attempt + 1)
            print(f"status {response.status_code} at {coor}, retry in {wait}s")
            time.sleep(wait)
        else:
            print(f"status {response.status_code} at {coor}")
            return []                          # other err (404)

    print(f"Gave up on {coor}")
    return []

def scrape_all(coords):
    """Scrape all coordinates concurrently using a thread pool."""
    all_stores = []
    total = len(coords)
    done = 0

    with ThreadPoolExecutor(max_workers=8) as executor: # 8 concurrent requests
        futures = [executor.submit(get_store_locs, c) for c in coords]
        
        for future in as_completed(futures):
            stores = future.result()
            all_stores += stores
            done += 1
            print(f"{done} / {total}")

    return all_stores


@timer
def main():
    """Load all-Canada coordinates, add city grids, dedupe, and scrape."""

    # Base coordinates: all Canada from postal codes
    zips = pd.read_csv(config.INPUT_COORDS)
    zips = zips[["latitude", "longitude"]].drop_duplicates()
    base_coords = list(zip(zips["latitude"], zips["longitude"]))
    
    # Add dense grids for major cities (to bypass the 50-store limit)
    city_coords = build_city_grids()

    # Combine and dedupe
    all_coords = list(set(base_coords + city_coords))
    print(f"Total coordinates: {len(all_coords)}")

    all_stores = scrape_all(all_coords)

    # Build DataFrame, dedupe by store_id, keep only Canadian stores
    df = pd.DataFrame(all_stores)
    df = df.drop_duplicates(subset="store_id").reset_index(drop=True)
    df = df[df["country"] == "CA"].reset_index(drop=True)
    print(df["province_code"].value_counts())
    df.to_csv(config.STORES_CSV, index=False, encoding="utf-8-sig")
    print(f"Total stores: {len(df)} stores")

if __name__ == "__main__":
    main()