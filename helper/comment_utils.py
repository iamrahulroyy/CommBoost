import openai
import re
from helper.config import GROQ_API_KEY, MODEL_NAME
from openai import OpenAIError

client = openai.OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def clean_comment(comment: str) -> str:
    comment = comment.strip().strip('"')
    comment = re.sub(r'[\\]+', '', comment)
    return comment

def generate_comment(post_text: str) -> str:
    if not post_text or len(post_text.strip()) < 5:
        return "Please provide a more detailed post for a meaningful comment."

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly and helpful commenter on professional posts. "
                        "Avoid generic phrases like 'great post' or 'thanks for sharing'. "
                        "Instead, write a short, thoughtful comment that feels natural, and try to make it specific to the topic."
                        "READ THE COMMENTS CAREFULLY TO KNOW MORE ABOUT THE POST AND FILL UP MISSING WORDS"
                        "AVOID THIS YPE OF WRITINGS [specific topic or section of the post] INSTAED FILL THIS UP WITH MEANINGFULL WORDS"
                    )
                },
                {
                    "role": "user",
                    "content": post_text.strip()
                }
            ],
            max_tokens=100,
            temperature=0.7
        )
        return clean_comment(response.choices[0].message.content)

    except OpenAIError as e:
        return f"Groq API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
