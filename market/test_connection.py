import os
import sys
from pprint import pprint
from dotenv import load_dotenv

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

load_dotenv()

if __name__ == "__main__":
    import upstox_client

    token = os.getenv("UPSTOX_ACCESS_TOKEN")
    if not token:
        print("⚠️ UPSTOX_ACCESS_TOKEN not found in environment.")
    else:
        configuration = upstox_client.Configuration()
        configuration.access_token = token
        api_client = upstox_client.ApiClient(configuration)
        market_api = upstox_client.MarketQuoteApi(api_client)

        try:
            response = market_api.get_full_market_quote(
                "NSE_EQ|INE009A01021",
                "2.0"
            )
            print("SUCCESS: Market Quote Retrieved!")
            pprint(response)
        except Exception as e:
            print(f"ERROR connecting to Upstox: {e}")