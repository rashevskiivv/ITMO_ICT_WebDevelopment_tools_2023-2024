from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os

from migrations.env import config

load_dotenv('.env')
db_url = os.getenv('DB_URL')
print(db_url)
config.set_main_option('sqlalchemy.url', db_url)
engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
