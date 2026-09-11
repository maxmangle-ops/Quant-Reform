import os
from dotenv import load_dotenv
import upstox_client

load_dotenv()

if __name__ == "__main__":
    token = os.getenv("UPSTOX_ACCESS_TOKEN")
    if not token:
        print("⚠️ UPSTOX_ACCESS_TOKEN not found in environment.")
    else:
        configuration = upstox_client.Configuration()
        configuration.access_token = token

        client = upstox_client.ApiClient(configuration)
        api = upstox_client.OptionsApi(client)

        print("=" * 80)
        print("REQUESTING OPTION CONTRACTS")
        print("=" * 80)

        try:
            response = api.get_option_contracts(
                instrument_key="NSE_INDEX|Nifty 50"
            )
            print("\nStatus:")
            print(getattr(response, "status", "Unknown"))
            print("\nResponse Type:")
            print(type(response.data))
            if hasattr(response, "data") and response.data:
                print(f"Contracts count: {len(response.data)}")
                print(f"First contract: {response.data[0]}")
        except Exception as e:
            print(f"Error requesting option contracts: {e}")