import logging
from fastapi import APIRouter
from helper.comment_utils import generate_comment
from helper.models import PostInput

router = APIRouter()

@router.post("/generate-comment/")
async def generate_ai_comment(data: PostInput):
    logging.info(f"Received content: {data.content[:100]}")
    comment = generate_comment(data.content)
    return {"comment": comment}