from fastapi import FastAPI
import subprocess
import os
import signal

app = FastAPI()

process = None


@app.get("/")
def home():
    return {"status": "alive"}


@app.get("/start")
def start():
    global process

    if process and process.poll() is None:
        return {"msg": "already running"}

    process = subprocess.Popen(["python", "strategy.py"])

    return {"msg": "started", "pid": process.pid}


@app.get("/stop")
def stop():
    global process

    if process and process.poll() is None:
        process.terminate()
        return {"msg": "stopped"}

    return {"msg": "not running"}


@app.get("/status")
def status():
    global process

    if process and process.poll() is None:
        return {"running": True, "pid": process.pid}

    return {"running": False}
