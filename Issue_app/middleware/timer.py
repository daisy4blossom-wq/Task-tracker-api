import time
from fastapi import Request

async def timing_request(request:Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}sec"
    return response

