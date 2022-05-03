from fastapi import FastAPI

import models

from db.session import engine

app = FastAPI(
    debug=True,
    title="Grades|Dataset"
)

@app.on_event("startup")
def init_db():
    """Creates table defined in models.py.
    """
    models.Base.metadata.create_all(engine)
