from app.extensions import db
from app.models import Favorite

def is_favorite(user_id, product_id):

    favorite = Favorite.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    return favorite is not None

def add_favorite(user_id, product_id):

    favorite = Favorite.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if favorite:
        return False

    new_favorite = Favorite(
        user_id=user_id,
        product_id=product_id
    )

    db.session.add(new_favorite)
    db.session.commit()

    return True

def remove_favorite(user_id, product_id):

    favorite = Favorite.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if favorite is None:
        return False

    db.session.delete(favorite)
    db.session.commit()

    return True

def get_user_favorites(user_id):

    return Favorite.query.filter_by(
        user_id=user_id
    ).order_by(
        Favorite.created_at.desc()
    ).all()