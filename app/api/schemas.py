from pydantic import BaseModel


class Grade(BaseModel):
    """Grade schema used to return data from the API.

    Args:
        BaseModel: Main pydantic model
    """

    id: int
    school_name: str
    category: str
    total_enrollment: int
    grade_k: int
    grade_1: int
    grade_2: int
    grade_3: int
    grade_4: int
    grade_5: int
    grade_6: int
    grade_7: int
    grade_8: int
    total_female: int
    ratio_female: float
    total_male: int
    ratio_male: float

    class Config:
        orm_mode = True
