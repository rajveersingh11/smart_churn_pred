from sqlalchemy import create_engine, text
from app.core.config import DB_URL

engine = create_engine(DB_URL)


