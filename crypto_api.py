import requests
def crypto():
    try:
        resp = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd",
            timeout=10,
        )
        resp.raise_for_status()
        prices = resp.json()
        btc_price = prices.get("bitcoin", {}).get("usd")
        eth_price = prices.get("ethereum", {}).get("usd")
        if btc_price is None or eth_price is None:
            return "Crypto prices unavailable."
        return f"Current Prices:\nBitcoin (BTC): ${btc_price}\nEthereum (ETH): ${eth_price}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching crypto prices: {e}"