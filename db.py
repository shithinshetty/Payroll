from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "etl", "payroll_analytics.db")

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=False
)

Session = sessionmaker(bind=engine)
