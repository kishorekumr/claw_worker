import time
import requests
import os

RUNNING = True

def main():
    print("Strategy process started")

    while RUNNING:
        try:
            # replace with your broker API
            res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            print("Data:", res.json())
        except Exception as e:
            print("Error:", e)

        time.sleep(5)

if __name__ == "__main__":
    main()
