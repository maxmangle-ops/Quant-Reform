import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from market.historical import get_historical_dataframe

if __name__ == "__main__":
    df = get_historical_dataframe("INFY")
    print(df.tail())
    print()
    print("Rows:", len(df))