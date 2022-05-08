import os
from typing import Optional

from celery import Celery
from db.dataset import clean
from db.session import write_to_db

celery = Celery(__name__)

celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@celery.task(name="load_dataset")
def load_dataset(dataset_url: str) -> Optional[int]:
    """Loads the dataset in the background.

    Args:
        dataset_url (str): The url to the dataset.

    Returns:
        None|int: The number of rows affected or None.
    """

    data = clean(dataset_url)
    
    return write_to_db(dataframe=data)
