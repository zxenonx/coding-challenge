from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import settings
import pandas as pd

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

table = "grades"


def write_to_db(dataframe: pd.DataFrame) -> None:
    """_summary_

    Args:
        dataframe (pd.DataFrame): _description_
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
    except ValueError as error:
        raise(error)
    else:
        print("data", rows_affected)
    finally:
        connection.close()
