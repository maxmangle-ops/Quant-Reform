import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from market.historical import get_historical_dataframe
from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.atr import calculate_atr
from indicators.vwap import calculate_vwap

if __name__ == "__main__":
    df = get_historical_dataframe("INFY")

    if not df.empty:
        # Indicators
        df["EMA20"] = calculate_ema(df["close"], 20)
        df["EMA50"] = calculate_ema(df["close"], 50)
        df["RSI14"] = calculate_rsi(df["close"])
        df["ATR14"] = calculate_atr(df["high"], df["low"], df["close"])
        df["VWAP"] = calculate_vwap(df["high"], df["low"], df["close"], df["volume"], df["time"])

        print("\n========== LATEST MARKET DATA ==========\n")
        print(df.tail(10))
        print("\nLatest Candle:\n")
        print(df.iloc[-1])
    else:
        print("No historical data returned (API token or market offline).")