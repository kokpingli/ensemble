from fastapi import FastAPI

from .api import sections

app = FastAPI(title="Ensemble API")

# Register routers
app.include_router(sections.router, prefix="/api")
