import requests

API_KEY = "2a9504dc1a5211f1a4e30242ac120002"

def get_market_value(year, make, model, condition, value_type="Dealer Retail"):
    url = f"https://api.vehicledatabases.com/market-value/v2/ymm/{year}/{make}/{model}"

    headers = {
        "x-authkey": API_KEY
    }

    condition = condition.capitalize()

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("status") != "success":
        raise ValueError("API returned an error: " + str(data))

    # Navigate into the JSON structure
    trims = data["data"]["market_value"]["market_value_data"]

    # Pick the first trim
    first_trim = trims[0]

    # Find the condition entry
    for entry in first_trim["market value"]:
        if entry["Condition"] == condition:
            return entry[value_type]

    raise ValueError(f"{condition} condition not found in response.")



