# extract.py
""" Docstring """

import os
import pandas as pd
from sqlalchemy import create_engine
from etl.utils.db_config import config

# from etl.constants import UTILS_DIR, RESOURCES_DIR
from etl import UTILS_DIR, RESOURCES_DIR  # porque existe __init__.py en etl/


def get_data_from_database():
    """Docstring"""

    engine = create_engine(
        "mssql+pymssql://{user}:{password}@{host}/{database}".format(**params)
    )

    with engine.connect().execution_options(autocommit=True):
        stmt = "SELECT * FROM ct_clientes"
        records = engine.execute(stmt)
        cols = records.keys()
        df = pd.DataFrame(records, columns=cols)

    df.to_csv(csv_raw, encoding="utf-8", index=False)


if __name__ == "__main__":

    csv_raw = os.path.join(RESOURCES_DIR, "ct_clientes_raw.csv")
    configuration_file = os.path.join(UTILS_DIR, "database.ini")
    params = config(filename=configuration_file, section="Argensun-Prueba")

    get_data_from_database()
