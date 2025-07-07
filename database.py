# app/models/database.py
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import settings

# Create SQLAlchemy async engine
engine = create_async_engine(settings.DATABASE_URL, echo=False)  # type: ignore

# Create Base class for models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    interactions = relationship("Interaction", back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    video_link = Column(String)
    category_id = Column(Integer)
    tags = Column(String)
    view_count = Column(Integer)
    interactions = relationship("Interaction", back_populates="post")

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    action = Column(String)
    value = Column(Float, nullable=True)
    user = relationship("User", back_populates="interactions")
    post = relationship("Post", back_populates="interactions")