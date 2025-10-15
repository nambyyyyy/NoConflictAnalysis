from fastapi import FastAPI
from presentation.api.v1.routers.events_router import router as events_router
from presentation.api.v1.routers.conflicts_router import router as conflicts_router

app = FastAPI(title="Analytics Service")

app.include_router(events_router, prefix="/v1")
app.include_router(conflicts_router, prefix="/v1")