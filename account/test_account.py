import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from account.account_models import Account
from account.account_manager import AccountManager

if __name__ == "__main__":
    manager = AccountManager()

    account = Account(
        broker="UPSTOX",
        available_cash=20000,
        available_margin=19500,
        used_margin=500,
        buying_power=100000,
        pnl_today=240,
        open_positions=1,
        holdings=3,
        open_orders=2,
    )

    manager.update(account)
    manager.print_summary()