"""e2e-fastapi-azure — FastAPI microservice."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="e2e-fastapi-azure",
    description="E2E test: FastAPI on Azure",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    service: str
    status: str
    cloud: str
    cost_center: str


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        service="e2e-fastapi-azure",
        status="UP",
        cloud="azure",
        cost_center="MC-100042",
    )


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to e2e-fastapi-azure"}
