"""
=========================================================
QUANT ULTRA
Option Execution Pipeline
=========================================================
Builds a complete option TradePlan.
=========================================================
"""

from market.option_chain import OptionChainEngine
from options.option_selector import OptionSelector
from execution.option_adapter import OptionAdapter
from utils.model_helper import ModelHelper


class OptionPipeline:

    def __init__(self):

        self.chain = OptionChainEngine()
        self.selector = OptionSelector()
        self.adapter = OptionAdapter()

    # -------------------------------------------------

    def execute(

        self,

        analysis,

        capital,

        risk_percent,

    ):

        print()
        print("=" * 60)
        print("📈 OPTION EXECUTION PIPELINE")
        print("=" * 60)

        underlying_symbol = str(
            ModelHelper.get(analysis, "symbol", "NIFTY")
        ).upper()

        key_map = {
            "NIFTY": "NSE_INDEX|Nifty 50",
            "BANKNIFTY": "NSE_INDEX|Nifty Bank",
            "SENSEX": "BSE_INDEX|SENSEX",
            "INFY": "NSE_EQ|INE009A01021",
        }
        instrument_key = key_map.get(
            underlying_symbol,
            f"NSE_INDEX|{underlying_symbol}",
        )

        try:
            contracts = self.chain.get_contracts(instrument_key)
        except Exception as e:
            print(f"⚠️ Failed to fetch option contracts: {e}")
            contracts = []

        candidate = self.selector.select(

            contracts=contracts,

            spot_price=ModelHelper.get(analysis, "price"),

            trend=ModelHelper.get(analysis, "trend"),

            technical_score=ModelHelper.get(analysis, "technical_score"),

            underlying=ModelHelper.get(analysis, "symbol"),

        )

        if candidate is None:

            raise Exception(
                "No suitable option contract found."
            )

        print()
        print("Selected Contract")
        print("----------------------------")
        print(candidate.contract.trading_symbol)
        print(candidate.contract.instrument_key)

        # -------------------------------------------------
        # Execution Side
        # -------------------------------------------------

        signal = str(
            ModelHelper.get(
                analysis,
                "signal",
                "BUY",
            )
        ).upper()

        # TEST MODE fallback
        if signal not in ("BUY", "SELL"):
            signal = "BUY"

        print()
        print("=" * 60)
        print("OPTION PIPELINE DEBUG")
        print("=" * 60)
        print("Analysis Signal :", ModelHelper.get(analysis, "signal"))
        print("Side Sent       :", signal)
        print("=" * 60)

        trade = self.adapter.create_trade(

            candidate=candidate,

            capital=capital,

            risk_percent=risk_percent,

            atr=ModelHelper.get(
                analysis,
                "atr",
            ),

            symbol=candidate.contract.trading_symbol,

            side=signal,

        )

        return trade, candidate
