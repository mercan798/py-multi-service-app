import requests
def currency():
    try:
        resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        eur_rate = data.get("rates", {}).get("EUR")
        gbp_rate = data.get("rates", {}).get("GBP")
        if eur_rate is None or gbp_rate is None:
            return "Currency rates unavailable."
        return f"1 USD is equal to {eur_rate} EUR and {gbp_rate} GBP."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching currency data: {e}"