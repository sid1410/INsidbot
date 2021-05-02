from sqlalchemy import (Table, Column, Integer, ForeignKey,
                        create_engine, String, DateTime)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Chat(Base):
    __tablename__ = 'chat'
    chatid = Column(Integer, primary_key=True)
    telegramid = Column(Integer, nullable=False)
    packid = Column(Integer, ForeignKey('pack.packid'))
    availedsolutions = Column(Integer, default=0)
    packpurchasedate = Column(DateTime)
    pack = relationship('Pack')


class Pack(Base):
    __tablename__ = 'pack'
    packid = Column(Integer, primary_key=True)
    packprice = Column(Integer, nullable=False)
    solutions = Column(Integer, nullable=False)

