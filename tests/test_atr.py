import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from indicators.atr import calculate_atr

if __name__ == "__main__":
    high = [
        10, 11, 12, 13, 14,
        15, 16, 17, 18, 19,
        20, 21, 22, 23, 24,
        25, 26, 27, 28, 29,
    ]

    low = [
        9, 10, 11, 12, 13,
        14, 15, 16, 17, 18,
        19, 20, 21, 22, 23,
        24, 25, 26, 27, 28,
    ]

    close = [
        9.5, 10.5, 11.5, 12.5, 13.5,
        14.5, 15.5, 16.5, 17.5, 18.5,
        19.5, 20.5, 21.5, 22.5, 23.5,
        24.5, 25.5, 26.5, 27.5, 28.5,
    ]

    atr = calculate_atr(high, low, close)

    print(atr)