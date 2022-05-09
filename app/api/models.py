from sqlalchemy import Column, Integer, String, Float, Identity
from db.session import Base


class Grade(Base):
    """Holds Grade's model attributes.

    Args:
        Base: Base class model from sqlalchemy
    """

    __tablename__ = "grades"

    id = Column("id", Integer, Identity(start=1, cycle=True), primary_key=True)
    school_name = Column(String)
    category = Column(String)
    total_enrollment = Column(Integer)
    grade_k = Column(Integer)
    grade_1 = Column(Integer)
    grade_2 = Column(Integer)
    grade_3 = Column(Integer)
    grade_4 = Column(Integer)
    grade_5 = Column(Integer)
    grade_6 = Column(Integer)
    grade_7 = Column(Integer)
    grade_8 = Column(Integer)
    total_female = Column(Integer)
    ratio_female = Column(Float)
    total_male = Column(Integer)
    ratio_male = Column(Float)
