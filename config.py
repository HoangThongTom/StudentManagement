from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "student_management_secret_key")

    password = quote_plus(os.getenv("MYSQL_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{os.getenv('MYSQL_USER')}:{password}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}"
        f"/{os.getenv('MYSQL_DB')}?charset=utf8mb4"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False