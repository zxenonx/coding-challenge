import api.models as models
from config import settings
from db.session import SessionLocal, engine
from fastapi import FastAPI
from worker import load_dataset

app = FastAPI(debug=True, title="Grades|Dataset")


@app.on_event("startup")
async def init_db():
    """Creates table defined in models.py."""
    models.Base.metadata.create_all(engine)

    # load dataset into table "grades"
    load_dataset.delay(settings.DATASET_URL)


# dependency
def get_db():
    """_summary_

    Yields:
        _type_: _description_
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
