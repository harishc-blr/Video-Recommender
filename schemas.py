# app/models/schema.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    picture_url = Column(String, nullable=True)
    user_type = Column(String)
    has_evm_wallet = Column(String)
    has_solana_wallet = Column(String)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    video_link = Column(String)
    thumbnail_url = Column(String)
    gif_thumbnail_url = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    comment_count = Column(Integer, default=0)
    upvote_count = Column(Integer, default=0)
    view_count = Column(Integer, default=0)
    exit_count = Column(Integer, default=0)
    average_rating = Column(Integer, default=0)
    bookmark_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
    tags = Column(String)

    owner = relationship("User", back_populates="posts")

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
