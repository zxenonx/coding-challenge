from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import settings
import pandas as pd

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

table = "grades"


def write_to_db(dataframe: pd.DataFrame) -> Optional[int]:
    """Inserts dataframe into database.

    Args:
        dataframe (pd.DataFrame): The dataframe to be inserted.

    Returns: 
        None or the number of rows affected.

    Raises:
        SQLAlchemyError: An error occurred while accessing the database.
    """
    rows_affected = 0
    connection = engine.connect()
    try:
        rows_affected = dataframe.to_sql(
            name=table,
            con=connection,
            if_exists="replace",
            index=True,
            index_label="id"
        )
    except SQLAlchemyError as error:
        raise(error)
    else:
        return rows_affected
    finally:
        connection.close()
