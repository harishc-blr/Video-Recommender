# app/api/routes/data.py
from fastapi import APIRouter, Query, Header
from app.services.data_fetcher import DataFetcher
from typing import List, Dict, Any

router = APIRouter(prefix="/data", tags=["Data Collection"])

@router.get("/posts/view", response_model=List[Dict[str, Any]])
async def get_viewed_posts(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), flic_token: str = Header(...)):
    fetcher = DataFetcher()
    return await fetcher.fetch_viewed_posts(page, page_size)

@router.get("/posts/like", response_model=List[Dict[str, Any]])
async def get_liked_posts(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), flic_token: str = Header(...)):
    fetcher = DataFetcher()
    return await fetcher.fetch_liked_posts(page, page_size)

@router.get("/posts/inspire", response_model=List[Dict[str, Any]])
async def get_inspired_posts(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), flic_token: str = Header(...)):
    fetcher = DataFetcher()
    return await fetcher.fetch_inspired_posts(page, page_size)

@router.get("/posts/rating", response_model=List[Dict[str, Any]])
async def get_rated_posts(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), flic_token: str = Header(...)):
    fetcher = DataFetcher()
    return await fetcher.fetch_rated_posts(page, page_size)