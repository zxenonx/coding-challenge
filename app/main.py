from fastapi import FastAPI
from worker import load_dataset
from config import settings

import api.models as models

from db.session import engine

app = FastAPI(debug=True, title="Grades|Dataset")


@app.on_event("startup")
async def init_db():
    """Creates table defined in models.py."""
    models.Base.metadata.create_all(engine)

    # load dataset into table "grades"
    load_dataset.delay(settings.DATASET_URL)
