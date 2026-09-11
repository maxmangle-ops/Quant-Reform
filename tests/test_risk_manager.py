import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from risk.risk_manager import calculate_position

if __name__ == "__main__":
    trade = calculate_position(
        entry_price=1094.20,
        atr=1.74,
        available_cash=100000,
        risk_percent=1,
    )

    print()
    print("===== RISK REPORT =====")

    for k, v in trade.items():
        print(f"{k}: {v}")