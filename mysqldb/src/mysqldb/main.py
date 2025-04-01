"""Main module for MySQLDB."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mysqldb.api.routers import items
from mysqldb.config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "MySQL Database API",
    description = "API for MySQL database operations",
    version = "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)

@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "Welcome to the MySQL Database API!"}

@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}
