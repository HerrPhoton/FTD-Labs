import os

from dotenv import load_dotenv

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

env_path = os.path.join(PROJECT_ROOT, ".env")
load_dotenv()

POSTS_URL = os.getenv("POSTS_URL")
