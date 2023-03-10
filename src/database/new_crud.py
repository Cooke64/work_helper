from database.news_model import NewsPost
from main import session


def show_limit_news() -> list[NewsPost]:
    return session.query(NewsPost).order_by(
        NewsPost.created_on.desc()
    ).limit(10).all()


def create_news_item(title: str, text: str,
                     photo_id: int | None = None) -> None:
    news_item = NewsPost(
        title=title,
        text=text,
        photo_id=photo_id
    )
    session.add(news_item)
    session.commit()


def updat_post(post_title: str, photo_id: int, text=None):
    post: NewsPost = session.query(NewsPost).filter(
        NewsPost.title == post_title).first()
    if post:
        post.photo_id = photo_id
        session.commit()
    else:
        create_news_item(post_title, text, photo_id)


def delete_post(post_title: str) -> None:
    post = session.query(NewsPost).filter(
            NewsPost.title.ilike(f'%{post_title}%')
    ).first()
    session.delete(post)
    session.commit()
