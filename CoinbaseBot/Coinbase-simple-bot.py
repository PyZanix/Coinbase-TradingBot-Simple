# Creator: Zanic/Ep4lf
# if you enjoy using this bot, feel free to text me on discord @ep4lr

import requests
import json
import time

# Coinbase API endpoints
BASE_URL = "https://api.coinbase.com/v2/"
BUY_PATH = "trades/buy"
SELL_PATH = "trades/sell"

# Coinbase API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Crypto currency to trade
CRYPTO_SYMBOL = 'BTC-USD'  # Example: Bitcoin to USD

# User's Coinbase wallet address
USER_WALLET_ADDRESS = 'your_wallet_address'

# Function to get current price of the cryptocurrency
def get_current_price():
    url = BASE_URL + f"prices/{CRYPTO_SYMBOL}/spot"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data['data']['amount'])
    else:
        print("Error fetching current price.")
        return None

# Function to place a buy order
def place_buy_order(amount):
    url = BASE_URL + BUY_PATH
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "amount": amount,
        "currency_pair": CRYPTO_SYMBOL
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Buy order placed successfully.")
    else:
        print("Error placing buy order.")

# Function to place a sell order
def place_sell_order(amount):
    url = BASE_URL + SELL_PATH
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "amount": amount,
        "currency_pair": CRYPTO_SYMBOL
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Sell order placed successfully.")
        print("Funds sent to your wallet address:", USER_WALLET_ADDRESS)
    else:
        print("Error placing sell order.")

# Main function
def main():
    while True:
        current_price = get_current_price()
        if current_price is not None:
            # Simulate buying at a low point
            if current_price < 100:  # Example threshold for a "low point"
                buy_amount = 100  # Example amount to buy
                place_buy_order(buy_amount)

            # Simulate selling when price goes up by 10%
            elif current_price >= 110:  # 10% increase from the buying price
                sell_amount = 100  # Example amount to sell
                place_sell_order(sell_amount)

        # Pause for some time before checking again
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
