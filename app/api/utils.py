from typing import Optional

from sqlalchemy.orm import Session

from .models import Grade


def fetch_grades(
    db: Session,
    category: Optional[str] = None,
    min_female: Optional[int] = None,
    max_female: Optional[int] = None,
    min_male: Optional[int] = None,
    max_male: Optional[int] = None,
):
    """Queries Grade's table and filters according to the parameters.

    Args:
        db (Session): SQLAlchemy session.
        category (Optional[str], optional): Filter for category. Defaults to None.
        min_female (Optional[int], optional): Filter for :value greater than or equal total_female. Defaults to None.
        max_female (Optional[int], optional): Filter for :value less than or equal total_female. Defaults to None.
        min_male (Optional[int], optional): Filter for :value greater than or equal total_male. Defaults to None.
        max_male (Optional[int], optional): Filter for :value less than or equal total_male. Defaults to None.

    Returns:
        _type_: _description_
    """

    query = db.query(Grade)

    if not (category or min_female or max_female or min_male or max_male):
        return query.all()

    if category:
        query = query.filter(Grade.category == category)

    if min_female:
        query = query.filter(Grade.total_female >= min_female)

    if max_female:
        query = query.filter(Grade.total_female <= max_female)

    if min_male:
        query = query.filter(Grade.total_male >= min_male)

    if max_male:
        query = query.filter(Grade.total_male <= max_male)

    return query.all()
