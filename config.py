import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


