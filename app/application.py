import uvicorn
import time
import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from logtc import Logtc, logtc_context, sockettc
from app.routes.test import router as test_router

app = FastAPI()
Logtc().setup(name="test")
Logtc().setup_file_handler(file_path="../log/.log", when="M", interval=1)
Logtc().setup_socket_handler(url="http://localhost:8000", handshake_path="/logtc/socket.io")
Logtc().setup_stream_handler()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    logtc_context.set(request_id)

    start_time = time.time()
    Logtc().logger.debug("%s", request.url.path)
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    Logtc().logger.info("%s", process_time)
    return response


@app.exception_handler(Exception)
async def uvicorn_exception_handler(request: Request, exc: Exception):
    logtc_context.set(request.state.request_id)
    Logtc().logger.error("error", exc_info=True)


app.include_router(test_router)

app.mount("/logtc", sockettc())


def test():
    import time
    logtc_context.set("11111111")
    while True:
        time.sleep(1)
        Logtc().logger.debug("11111111")


def test2():
    import time
    logtc_context.set("2222222")
    while True:
        time.sleep(1)
        Logtc().logger.debug("2222222")


if __name__ == "__main__":
    import threading

    # thread = threading.Thread(target=test, args=())
    # thread.daemon = True
    # thread.start()
    #
    # thread2 = threading.Thread(target=test2, args=())
    # thread2.daemon = True
    # thread2.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
