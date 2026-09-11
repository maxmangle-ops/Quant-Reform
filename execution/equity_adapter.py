"""
=========================================================
QUANT ULTRA
Equity Adapter
=========================================================
Converts Equity Analysis into TradePlan.
=========================================================
"""

from risk.risk_manager import calculate_position
from utils.model_helper import ModelHelper


class EquityAdapter:

    def __init__(self):
        pass

    # -------------------------------------------------

    def create_trade(
        self,
        analysis,
        capital,
        risk_percent,
    ):
        price = float(ModelHelper.get(analysis, "price", 0.0))
        atr = float(ModelHelper.get(analysis, "atr", 1.0))
        symbol = str(ModelHelper.get(analysis, "symbol", "UNKNOWN"))
        signal = str(ModelHelper.get(analysis, "signal", "BUY")).upper()
        side = "SELL" if signal == "SELL" else "BUY"

        return calculate_position(
            entry_price=price,
            atr=atr,
            available_cash=capital,
            buying_power=capital * 5,
            risk_percent=risk_percent,
            profile="BALANCED",
            symbol=symbol,
            side=side,
        )


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("EQUITY ADAPTER READY")

    print("=" * 60)