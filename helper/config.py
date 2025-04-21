import os
from dotenv import load_dotenv

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
