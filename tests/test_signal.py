import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from strategy.signal_engine import generate_signal

if __name__ == "__main__":
    signal = generate_signal(
        price=1090,
        ema20=1089,
        ema50=1088,
        rsi=62,
        vwap=1088.5,
        atr=1.5,
    )

    print(signal)