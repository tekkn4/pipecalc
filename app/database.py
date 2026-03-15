# app/database.py – Neon-kompatible Version
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import get_settings
import os

settings = get_settings()

# Für Vercel/Neon: pool_size=1, keine persistenten Connections
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=1,
    max_overflow=0,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
