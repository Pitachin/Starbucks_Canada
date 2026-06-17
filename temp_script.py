from city import make_grid
from scraper import scrape_all
import pandas as pd

toronto_finer = make_grid(43.6532, -79.3832, radius=0.4, step=0.02)
print(f"Points: {len(toronto_finer)}")
stores = scrape_all(toronto_finer)
df = pd.DataFrame(stores).drop_duplicates(subset="store_id")
print(f"Toronto (finer): {len(df)}")