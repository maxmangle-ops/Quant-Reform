import inspect
import upstox_client

if __name__ == "__main__":
    print("=" * 80)
    print("get_option_contracts")
    print("=" * 80)
    print(inspect.signature(upstox_client.OptionsApi.get_option_contracts))

    print()
    print("=" * 80)
    print("get_put_call_option_chain")
    print("=" * 80)
    print(inspect.signature(upstox_client.OptionsApi.get_put_call_option_chain))