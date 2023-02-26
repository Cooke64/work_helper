
from sqlalchemy import Column as _, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PhotosIds(Base):
    """
    Для хранения ID фотогрфий и описания к ним.
    photo_id это id файла, полученное от TG.
    filedescr описание файла, которое опционно может быть добавлено
    """
    __tablename__ = 'photos ids'
    id = _(Integer, primary_key=True)
    file_unique_id = _(String(255), nullable=False, unique=True)
    photo_id = _(String(255), nullable=False)
    filedescr = _(Text(), nullable=True)

    def __repr__(self) -> str:
        unique = self.file_unique_id
        return f"User(id={self.id!r}, file_id={self.file_id!r}, filedescr={self.filedescr}, unique={unique})"
