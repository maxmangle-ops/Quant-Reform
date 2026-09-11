from market.option_chain import OptionChainEngine
from options.option_selector import OptionSelector

if __name__ == "__main__":
    print("=" * 70)
    print("OPTION SELECTOR TEST")
    print("=" * 70)

    chain = OptionChainEngine()

    try:
        contracts = chain.get_contracts("NSE_INDEX|Nifty 50")
    except Exception as e:
        print(f"OptionChainEngine error: {e}")
        contracts = []

    selector = OptionSelector()

    candidate = selector.select(
        contracts=contracts,
        spot_price=24239.5,
        trend="BULLISH",
        technical_score=70,
        underlying="NIFTY",
    )

    if candidate is None:
        print("No contract selected")
    else:
        print()
        print("Selected Contract")
        print("----------------------------")
        print(candidate.contract.trading_symbol)
        print(candidate.contract.instrument_key)
        print(candidate.contract.strike)
        print(candidate.contract.option_type)
        print(candidate.contract.expiry)