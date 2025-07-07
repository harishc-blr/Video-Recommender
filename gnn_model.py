# app/ml/gnn_model.py
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
from typing import List

class GNNRecommender(torch.nn.Module):
    def __init__(self, num_users: int, num_posts: int, hidden_dim: int = 64):
        super(GNNRecommender, self).__init__()
        self.conv1 = GCNConv(num_users + num_posts, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.num_users = num_users
        self.num_posts = num_posts

    def forward(self, data: Data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

    def recommend(self, data: Data, user_id: int, top_k: int = 10) -> List[int]:
        self.eval()
        with torch.no_grad():
            embeddings = self.forward(data)
            user_embedding = embeddings[user_id]
            post_embeddings = embeddings[self.num_users:]
            scores = torch.matmul(post_embeddings, user_embedding)
            _, indices = torch.topk(scores, top_k)
            return indices.tolist()

    def train_model(self, data: Data, epochs: int = 100, lr: float = 0.01):
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        self.train()
        for epoch in range(epochs):
            optimizer.zero_grad()
            embeddings = self.forward(data)
            loss = self.compute_loss(embeddings, data)
            loss.backward()
            optimizer.step()
            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss.item()}")

    def compute_loss(self, embeddings: torch.Tensor, data: Data) -> torch.Tensor:
        # Placeholder for loss computation
        return torch.tensor(0.0)