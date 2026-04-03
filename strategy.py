import time

running = False

def run_strategy():
    global running
    running = True

    print("Strategy started")

    while running:
        # 👉 Replace with Zerodha logic
        print("Checking market...")
        time.sleep(5)

    print("Strategy stopped")


def stop_strategy():
    global running
    running = False
