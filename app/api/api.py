from typing import Optional

import schemas
from api.utils import fetch_grades
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.main import app, get_db


@app.get("/grades", response_model=list[schemas.Grade], status_code=200)
async def get_grades(
    category: Optional[str] = None,
    min_female: Optional[int] = None,
    max_female: Optional[int] = None,
    min_male: Optional[int] = None,
    max_male: Optional[int] = None,
    db: Session = Depends(get_db),
):
    data = fetch_grades(
        db,
        category=category,
        min_female=min_female,
        max_female=max_female,
        min_male=min_male,
        max_male=max_male,
    )

    if not data:
        raise HTTPException(status_code=404, detail="No results")

    return data
