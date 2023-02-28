from database.image_model import PhotosIds
from main import session


def get_all_photos():
    return session.query(PhotosIds).all()


def get_photo_by_unique_id(file_unique_id: str) -> PhotosIds:
    return session.query(PhotosIds).filter(
        PhotosIds.file_unique_id == file_unique_id).first()


def add_photo_in_db(
        photo_id: str,
        file_unique_id: str,
        caption: str | None = None
) -> bool:
    photo = get_photo_by_unique_id(file_unique_id)
    if not photo:
        new_instanse = PhotosIds(
            file_unique_id=file_unique_id,
            photo_id=photo_id,
            filedescr=caption
        )
        session.add(new_instanse)
        session.commit()
        return True
    return False
