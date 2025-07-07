from fastapi import FastAPI
from app.api.routes import feed, data
from app.config.settings import settings
from app.models.database import engine, Base
from app.services.cache import RedisCache

app = FastAPI(
    title="Video Recommendation Engine",
    description="A sophisticated video recommendation system using deep neural networks.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Recommendation",
            "description": "Endpoints for personalized and category-based video recommendations"
        },
        {
            "name": "Data Collection",
            "description": "Internal endpoints for fetching data from Socialverse APIs"
        }
    ]
)

# Include routers
app.include_router(feed.router)
app.include_router(data.router)


# Startup event: initialize DB and Redis
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    redis_cache = RedisCache()
    await redis_cache.client.ping()
    app.state.redis = redis_cache


# Shutdown event: close DB and Redis
@app.on_event("shutdown")
async def shutdown_event():
    await engine.dispose()
    if hasattr(app.state, "redis"):
        await app.state.redis.close()

from fastapi import APIRouter, Query




# Root endpoint
@app.get("/")
async def root():
    return {"message": "Video Recommendation Engine is running"}
