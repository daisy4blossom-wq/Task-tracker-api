from fastapi import FastAPI, HTTPException
from routes.issues import router as task_router
from pydantic import BaseModel
from middleware.timer import timing_request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timing_request)
app.include_router(task_router)

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"],)
