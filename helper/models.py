from pydantic import BaseModel, Field

class PostInput(BaseModel):
    content: str = Field(..., min_length=5, description="The content to analyze and generate a comment for.")
