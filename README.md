# 🎥 Video Recommendation Engine with Deep Learning

This project implements a personalized video recommendation system using **Graph Neural Networks (GNNs)**, **FastAPI**, and **PyTorch Geometric**, tailored for motivational content sourced from the Empowerverse App.

> ⚡️ Intelligent. Personalized. Scalable.

---

## 🚀 Features

- 📊 **Personalized recommendations** based on user interaction history
- 🧠 **Graph Neural Network (GNN)**-powered content modeling
- 💡 **Cold start handling** using category/mood-based fallback
- 🔗 **API-first architecture** using FastAPI
- 🌐 Integrated with external APIs for dynamic video content
- 🧪 Built-in training, inference, and recommendation pipeline

---

## 📂 Project Structure

video-recommendation-engine/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── models/ # SQLAlchemy models & database
│ ├── ml/ # GNN model implementation
│ ├── services/ # Data fetcher, recommender logic
│ └── api/ # Optional: routers/controllers
│
├── alembic/ # DB migrations
├── .env # Environment config
├── requirements.txt
├── README.md
└── ...

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/video-recommendation-engine.git
cd video-recommendation-engine
2. Create virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Setup the database
bash
Copy
Edit
alembic upgrade head
Ensure your .env contains correct DB and API keys.

5. Run the app
bash
Copy
Edit
uvicorn app.main:app --reload
API available at: http://localhost:8000/docs

🧠 Model Overview
Uses a Graph Neural Network (GNN) via PyTorch Geometric

Trains on user-post interaction graph: edges = interactions

Node features: Identity matrix (torch.eye)

Recommender outputs ranked post IDs based on learned embeddings

🧪 API Endpoints
Endpoint	Method	Description
/recommend/user/{username}	GET	Top-N recommendations for a user
/recommend/category/{project_code}	GET	Top-N videos from category fallback
/data/posts/rating	GET	Fetch external motivational videos
/train	POST	Trigger model training

🛠️ Technologies Used
FastAPI + Uvicorn

SQLAlchemy + Alembic

PostgreSQL (or SQLite for dev)

PyTorch + PyTorch Geometric

dotenv, Pydantic, requests

📌 TODOs / Improvements
 Add user feedback loop for recommendations

 Improve cold-start via sentiment/mood embeddings

 Add logging & monitoring (Prometheus/Grafana)

 Dockerize the full stack

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
Apache 2.0 License ©Harish C
 
