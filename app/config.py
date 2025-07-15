# app/config.py
# 환경변수 로드용 

from dotenv import load_dotenv
import os

load_dotenv()

def get_secret(key: str, default: str = None):
    return os.getenv(key, default)
