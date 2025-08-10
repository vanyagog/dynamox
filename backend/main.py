from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
successful_requests = 0

@app.middleware("http")
async def count_successful_requests(request: Request, call_next):
    global successful_requests
    response = await call_next(request)
    if 200 <= response.status_code < 300:
        successful_requests += 1
    return response

@app.get("/count")
async def get_count():
    return {"successful_requests": successful_requests}

@app.get("/")
async def root():
    return {"message": "OK"}
