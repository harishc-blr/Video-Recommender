from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/feed/", tags=["Recommendation"])
async def get_feed(username: str = Query(..., description="Username of the user")):
    # Return hardcoded post with Harish's details
    example_response = {
        "status": "success",
        "post": [
            {
                "id": 3104,
                "owner": {
                    "first_name": "Harish",
                    "last_name": "C",
                    "name": "Harish C",
                    "username": "harishc123",
                    "picture_url": "https://ui-avatars.com/api/?name=Harish+C&background=random",
                    "user_type": None,
                    "has_evm_wallet": False,
                    "has_solana_wallet": False
                },
                "category": {
                    "id": 13,
                    "name": "Flic",
                    "count": 125,
                    "description": "Where Creativity Meets Opportunity",
                    "image_url": "https://socialverse-assets.s3.us-east-1.amazonaws.com/categories/NEW_COLOR.png"
                },
                "topic": {
                    "id": 1,
                    "name": "Social Media",
                    "description": "Short form content making and editing.",
                    "image_url": "https://ui-avatars.com/api/?size=300&name=Social%20Media&color=fff&background=random",
                    "slug": "b9f5413f04ec58e47874",
                    "is_public": True,
                    "project_code": "flic",
                    "posts_count": 18,
                    "language": None,
                    "created_at": "2025-02-15 15:02:41",
                    "owner": {
                        "first_name": "Harish",
                        "last_name": "C",
                        "name": "Harish C",
                        "username": "harishc123",
                        "profile_url": "https://ui-avatars.com/api/?name=Harish+C&background=random",
                        "user_type": "creator",
                        "has_evm_wallet": False,
                        "has_solana_wallet": False
                    }
                },
                "title": "testing-topic",
                "is_available_in_public_feed": True,
                "is_locked": False,
                "slug": "0dcff38b97c646a37ebcfa4f039c332812aa3857",
                "upvoted": False,
                "bookmarked": False,
                "following": False,
                "identifier": "QCp8ffL",
                "comment_count": 0,
                "upvote_count": 4,
                "view_count": 235,
                "exit_count": 149,
                "rating_count": 0,
                "average_rating": 84,
                "share_count": 0,
                "bookmark_count": 0,
                "video_link": "https://video-cdn.socialverseapp.com/harish_sample_video.mp4",
                "thumbnail_url": "https://video-cdn.socialverseapp.com/harish_sample_video.0000002.jpg",
                "gif_thumbnail_url": "https://video-cdn.socialverseapp.com/harish_sample_video.gif",
                "contract_address": "",
                "chain_id": "",
                "chart_url": "",
                "baseToken": {
                    "address": "",
                    "name": "",
                    "symbol": "",
                    "image_url": ""
                },
                "created_at": 1739791247000,
                "tags": ["testing", "editing", "social-media"]
            }
        ]
    }

    return JSONResponse(content=example_response)

