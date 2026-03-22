import pandas as pd
from sqlalchemy import create_engine
import urllib.parse


def get_db_engine():
    raw_password = "Deepesh@20"
    safe_password = urllib.parse.quote_plus(raw_password)

    # Connection string
    connection_uri = f"mysql+pymysql://root:{safe_password}@localhost/credit_db"

    engine = create_engine(connection_uri)
    return engine
