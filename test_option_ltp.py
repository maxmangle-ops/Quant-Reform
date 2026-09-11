import os
import upstox_client
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    token = os.getenv("UPSTOX_ACCESS_TOKEN")
    if not token:
        print("⚠️ UPSTOX_ACCESS_TOKEN not found in environment.")
    else:
        configuration = upstox_client.Configuration()
        configuration.access_token = token
        client = upstox_client.ApiClient(configuration)
        api = upstox_client.MarketQuoteApi(client)

        print("=" * 70)
        print("OPTION LTP TEST")
        print("=" * 70)

        instrument = "NSE_FO|63949"
        try:
            response = api.ltp(
                symbol=instrument,
                api_version="2.0",
            )
            print(response)
        except Exception as e:
            print(f"Error fetching option LTP: {e}")