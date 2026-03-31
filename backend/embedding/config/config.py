import os
from dotenv import load_dotenv

# Load envriment variables from .env file
load_dotenv()

class Config:
    
    # Database configs
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_ENDPOINT = os.getenv("QDRANT_ENDPOINT")
    
    # AI MODEL from Hugging face
    MODEL_NAME = os.getenv("MODEL_NAME")

    # Collection name  / Table name in database
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "CHAT_BOT_COLLECTION")

    # Vector Size
    VECTOR_SIZE = 128
