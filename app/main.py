from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.test_connection import router as test_router
from app.api.customer_test import router as customer_router
from app.api.analysis import router as analysis_router

import app.models

app = FastAPI(
    title="Copiloto Analytics API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)
app.include_router(customer_router)
app.include_router(analysis_router)

@app.get("/health")
def health():
    return {
        "status": "ok"
    }