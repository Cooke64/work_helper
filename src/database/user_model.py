from datetime import datetime

from sqlalchemy import Column as _, Integer, String, DateTime, Boolean

from database.image_model import Base


class UserMessage(Base):
    __tablename__ = 'users'

    id = _(Integer(), primary_key=True)
    username = _(String(100), nullable=False, unique=True)
    message = _(String(100), nullable=True)
    created_on = _(DateTime(), default=datetime.now)
    passed_test = _(Boolean, default=False)
    can_serve = _(Boolean, default=False)
    phone = _(String(100), nullable=True)

    def __repr__(self) -> str:
        pk = self.id
        name = self.username
        mes = self.message
        serv = self.can_serve
        test = self.passed_test
        phone = self.phone
        return f"User(id={pk!r}," \
               f" username={name!r}," \
               f" message={mes!r}," \
               f"can_serve={serv!r}," \
               f" passed_test={test!r}," \
               f" phone={phone})"
