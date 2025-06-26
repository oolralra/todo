# routers/board.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
import os
from fastapi.encoders import jsonable_encoder
router = APIRouter()

# MongoDB 연결 (환경변수 또는 기본값)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["myapp"]
posts_collection = db["posts"]

# 게시글 모델
class Post(BaseModel):
    title: str
    content: str
    author: str

# 게시글 작성


@router.post("/posts/")
async def create_post(post: Post):
    try:
        post_dict = post.dict()
        post_dict["created_at"] = datetime.utcnow()
        result = await posts_collection.insert_one(post_dict)

        # 새로운 dict로 응답 구성
        response = {
            "id": str(result.inserted_id),
            "title": post.title,
            "content": post.content,
            "author": post.author,
            "created_at": post_dict["created_at"].isoformat(),
        }

        return response
    except Exception as e:
        print("게시글 작성 오류:", e)
        raise HTTPException(status_code=500, detail=str(e))



# 게시글 목록 조회
@router.get("/posts/")
async def list_posts():
    posts = []
    async for post in posts_collection.find():
        posts.append({
            "id": str(post["_id"]),
            "title": post["title"],
            "content": post["content"],
            "author": post["author"],
            "created_at": post["created_at"].isoformat() if "created_at" in post else None
        })
    return posts

