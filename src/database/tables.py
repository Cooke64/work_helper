from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserMessage(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    message = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    passed_test = Column(Boolean, default=False)
    can_serve = Column(Boolean, default=False)

    def __repr__(self) -> str:
        pk = self.id
        name = self.username
        mes = self.message
        serv = self.can_serve
        test = self.passed_test
        return f"User(id={pk!r}, username={name!r}, message={mes!r},can_serve={serv!r}, passed_test={test!r})"
