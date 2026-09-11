import os
import sys
import pandas as pd

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from indicators.vwap import calculate_vwap

if __name__ == "__main__":
    data = pd.DataFrame({
        "high": [10, 11, 12, 13, 14],
        "low": [9, 10, 11, 12, 13],
        "close": [9.5, 10.5, 11.5, 12.5, 13.5],
        "volume": [100, 120, 110, 130, 140],
    })

    vwap = calculate_vwap(
        data["high"],
        data["low"],
        data["close"],
        data["volume"],
    )

    print(vwap)