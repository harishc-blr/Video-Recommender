# app/services/data_fetcher.py
import httpx
from app.config.settings import settings
from app.services.cache import RedisCache
from typing import List, Dict, Any

class DataFetcher:
    def __init__(self):
        self.base_url = settings.API_BASE_URL
        self.headers = {"Flic-Token": settings.FLIC_TOKEN}
        self.cache = RedisCache()

    async def fetch_viewed_posts(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"viewed_posts_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/view?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_liked_posts(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"liked_posts_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/like?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_inspired_posts(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"inspired_posts_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/inspire?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_rated_posts(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"rated_posts_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/rating?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_all_posts(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"all_posts_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/summary?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_all_users(self, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"all_users_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/users?page={page}&page_size={page_size}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("users", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_user_data(self, username: str) -> Dict[str, Any]:
        cache_key = f"user_data_{username}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/users/{username}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            await self.cache.set(cache_key, data, expire=3600)
            return data

    async def fetch_posts_by_category(self, project_code: str, page: int, page_size: int) -> List[Dict[str, Any]]:
        cache_key = f"category_posts_{project_code}_{page}_{page_size}"
        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return cached_data
        url = f"{self.base_url}/posts/category/{project_code}?page={page}&page_size={page_size}&resonance_algorithm=personalized"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get("post", [])
            await self.cache.set(cache_key, data, expire=3600)
            return data