from fastapi import FastAPI
import threading
import strategy

app = FastAPI()

thread = None

@app.get("/")
def home():
    return {"status": "alive"}

@app.get("/start")
def start():
    global thread

    if thread and thread.is_alive():
        return {"message": "already running"}

    thread = threading.Thread(target=strategy.run_strategy)
    thread.start()

    return {"message": "started"}

@app.get("/stop")
def stop():
    strategy.stop_strategy()
    return {"message": "stopped"}

@app.get("/status")
def status():
    return {"running": strategy.running}
