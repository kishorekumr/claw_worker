from fastapi import FastAPI
import threading
import time
import requests

app = FastAPI()

running = False

def strategy():
    global running
    running = True

    while running:
        try:
            # 👉 Example API call (replace with your broker API)
            res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            data = res.json()
            print("Price:", data)

        except Exception as e:
            print("Error:", e)

        time.sleep(5)


@app.get("/")
def home():
    return {"status": "alive"}


@app.get("/start")
def start():
    global running

    if running:
        return {"msg": "already running"}

    t = threading.Thread(target=strategy)
    t.start()

    return {"msg": "started"}


@app.get("/stop")
def stop():
    global running
    running = False
    return {"msg": "stopped"}


@app.get("/status")
def status():
    return {"running": running}
