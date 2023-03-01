from datetime import datetime

from sqlalchemy import Column as _, Integer, String, DateTime, Text

from database.image_model import Base


class NewsPost(Base):
    __tablename__ = 'newspost'

    id = _(Integer(), primary_key=True)
    title = _(String(100), nullable=False)
    text = _(Text, nullable=False)
    created_on = _(DateTime(), default=datetime.now)
    photo_id = _(String(199), default=True)

    def __repr__(self) -> str:
        pk = self.id
        return f"NewsPost(id={pk!r}," \
               f"title={self.title!r}," \
               f" text={self.text!r}," \
               f" created_on={self.created_on!r}," \
               f" photo_id={self.photo_id!r},"
