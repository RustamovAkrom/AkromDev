from dotenv import load_dotenv

load_dotenv("envs/.env")

import os

if os.getenv("MODE") == "development":
    from .development import *
elif os.getenv("MODE") == "production":
    from .production import *
else:
    from .base import *
