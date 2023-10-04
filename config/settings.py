from typing import List

API_VERSIONS: List[str] = ["v1", "v2"]

DATABASE_URL: str = "sqlite:///./test.db"

JWT_SECRET_KEY: str = "your-secret-key"
JWT_ALGORITHM: str = "HS256"
JWT_EXPIRATION_TIME_MINUTES: int = 30

DEBUG: bool = True
