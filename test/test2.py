import threading
from requests import get


def make_request(path: str):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN0cmluZyIsInJvbGUiOiJBRE1JTiIsImV4cGlyZV90aW1lIjoxNzA0ODY5NjczfQ.tSCru_Bjwe3bcXI-N3nIZUaJ4vMG9AGgT0EImErKG-o'
    }
    for i in range(10000):
        try:
            resp = get(f"http://10.17.70.25:8005/{path}", headers=headers)
            print(path, resp.text, resp.headers['X-Process-Time'])
        except:
            pass


if __name__ == "__main__":
    high_thread = threading.Thread(target=make_request, args=("account/me",))
    # medium_thread = threading.Thread(target=make_request, args=("backup/env",))
    low_thread = threading.Thread(target=make_request, args=("account/get-all",))
    high_thread.start()
    # medium_thread.start()
    low_thread.start()
