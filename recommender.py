# app/services/recommender.py
from app.ml.gnn_model import GNNRecommender
from app.services.data_fetcher import DataFetcher
from app.models.database import engine, User, Post, Interaction
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from torch_geometric.data import Data
import torch
from typing import List, Dict, Any

class Recommender:
    def __init__(self):
        self.data_fetcher = DataFetcher()
        self.gnn_model: GNNRecommender | None = None

    async def initialize_model(self, num_users: int, num_posts: int):
        self.gnn_model = GNNRecommender(num_users, num_posts)
        await self.train_model()

    async def train_model(self):
        if self.gnn_model is None:
            raise ValueError("GNN model not initialized. Call initialize_model first.")
        
        async with AsyncSession(engine) as session:
            interactions = await session.execute(select(Interaction))
            interactions = interactions.scalars().all()

        # Create graph data
        edge_index = []
        for interaction in interactions:
            edge_index.append([interaction.user_id, self.gnn_model.num_users + interaction.post_id])
        edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
        x = torch.eye(self.gnn_model.num_users + self.gnn_model.num_posts)  # Simple identity features
        data = Data(x=x, edge_index=edge_index)

        # Train GNN model
        self.gnn_model.train_model(data)

    async def get_recommendations(self, username: str, top_k: int = 10) -> List[Dict[str, Any]]:
        if self.gnn_model is None:
            raise ValueError("GNN model not initialized. Call initialize_model first.")
        
        async with AsyncSession(engine) as session:
            result = await session.execute(select(User).filter_by(username=username))
            user = result.scalars().first()
            if not user:
                return []

            # Fetch all posts
            posts_result = await session.execute(select(Post))
            posts = posts_result.scalars().all()

            # Create graph data
            interactions = await session.execute(select(Interaction))
            interactions = interactions.scalars().all()
            edge_index = [[i.user_id, self.gnn_model.num_users + i.post_id] for i in interactions]
            edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
            x = torch.eye(self.gnn_model.num_users + self.gnn_model.num_posts)
            data = Data(x=x, edge_index=edge_index)

            # Get recommendations
            recommended_post_ids = self.gnn_model.recommend(data, top_k)
            recommended_posts = [post for post in posts if post.id in recommended_post_ids]
            return [{"id": post.id, "title": post.title, "video_link": post.video_link} for post in recommended_posts]

    async def get_category_recommendations(self, project_code: str, top_k: int = 10) -> List[Dict[str, Any]]:
        try:
            posts = await self.data_fetcher.fetch_posts_by_category(project_code, page=1, page_size=top_k)
            return posts[:top_k]
        except:
            return []  # Handle 404 or other API errors