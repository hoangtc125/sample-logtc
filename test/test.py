import threading
from requests import get


def make_request(path: str):
    for i in range(10000):
        try:
            resp = get(f"http://localhost:8000/{path}")
        except:
            pass


if __name__ == "__main__":
    high_thread = threading.Thread(target=make_request, args=("high",))
    medium_thread = threading.Thread(target=make_request, args=("medium",))
    low_thread = threading.Thread(target=make_request, args=("low",))
    high_thread.start()
    medium_thread.start()
    low_thread.start()
