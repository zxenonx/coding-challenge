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
    grade_k = Column(Float)
    grade_1 = Column(Float)
    grade_2 = Column(Float)
    grade_3 = Column(Float)
    grade_4 = Column(Float)
    grade_5 = Column(Float)
    grade_6 = Column(Float)
    grade_7 = Column(Float)
    grade_8 = Column(Float)
    total_female = Column(Integer)
    ratio_female = Column(Float)
    total_male = Column(Integer)
    ratio_male = Column(Float)
