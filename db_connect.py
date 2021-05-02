from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import dsn


def get_engine():
    engine = create_engine(dsn)
    return engine


def create_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = create_session()
