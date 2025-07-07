#   Video Recommendation Engine

A personalized recommendation system for motivational videos inspired by the Empowerverse App. Built using **FastAPI**, this engine delivers tailored content based on user engagement, handles **cold-start** scenarios, integrates with the **Socialverse API**, and uses **deep learning** (including **GNN**) to rank content effectively.

---

##  Features

-  Personalized video recommendations  
-  Hybrid recommendation system (Collaborative + Content-based + Graph Neural Network)  
-  Cold-start user support with mood-based video categories  
-  FastAPI backend with Swagger docs  
-  Redis caching and paginated API responses  
-  Integration with external APIs (via `FLIC_TOKEN`)  
-  Postman collection for testing  
-  Docker-ready architecture (optional)  

---

##  Project Structure

video-recommendation-engine/
├── app/
│   ├── init.py
│   ├── api/
│   │   ├── init.py
│   │   └── routes/
│   │       ├── init.py
│   │       ├── data.py
│   │       ├── feed.py
│   ├── config/
│   │   ├── init.py
│   │   └── settings.py
│   ├── models/
│   │   ├── init.py
│   │   └── database.py
│   ├── services/
│   │   ├── init.py
│   │   ├── cache.py
│   │   ├── data_fetcher.py
│   │   └── recommender.py
│   ├── ml/
│   │   ├── init.py
│   │   └── gnn_model.py
│   └── main.py
├── alembic/
│   ├── env.py
│   └── versions/
│       └── 2025_07_07_create_tables.py
├── .env
├── requirements.txt
└── README.md


---

##  Recommendation Strategy

The system uses a **hybrid recommendation approach** combining:

- **Collaborative Filtering**: Based on engagement (views, likes, inspires, ratings)  
- **Content-Based Filtering**: Based on tags, categories, and metadata  
- **Graph Neural Network (GNN)**:
  - Nodes = Users + Posts  
  - Edges = Interactions (view, like, rate, inspire)  
  - GCN predicts relevance score between a user and post  
- **Cold Start**: Recommends top motivational posts from categories like “Flic”, “Productivity”, “Inspiration”

---

## 🌐 API Endpoints

All endpoints return JSON responses following:
```json
{
  "status": "success",
  "post": [
    {
      "id": 1,
      "title": "Your Mind is Powerful",
      "video_link": "https://...",
      "tags": ["growth", "productivity"],
      "category": "motivation"
    }
  ]
}

GET /feed?username={username}
Returns personalized recommendations based on user's past interactions.
GET /feed?username={username}&project_code={project_code}
Returns filtered recommendations using both user preferences and selected project category.

