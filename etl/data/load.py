# load.py
""" Docstring """

import os
from sqlalchemy import create_engine, MetaData, Table, delete
import pandas as pd

# from etl.utils.db_config import config
# from etl.constants import UTILS_DIR, RESOURCES_DIR
from etl import (
    config,
)  # porque existe __init__.py en el root del paquete y en etl/utils/
from etl import UTILS_DIR, RESOURCES_DIR  # porque existe __init__.py en etl/


def load_data_to_database(df):
    """Docstring"""

    engine = create_engine(
        "mysql+pymysql://{user}:{password}@{host}/{database}".format(**params)
    )

    metadata = MetaData(bind=engine)

    with engine.connect().execution_options(autocommit=True) as conn:
        ost_list_items_table = Table("ost_list_items", metadata, autoload_with=engine)
        stmt = delete(ost_list_items_table).where(ost_list_items_table.c.list_id == 10)
        conn.execute(stmt)
        df.to_sql("ost_list_items", con=conn, if_exists="append", index=False)


if __name__ == "__main__":

    csv_file = os.path.join(RESOURCES_DIR, "ct_clientes_transform.csv")
    configuration_file = os.path.join(UTILS_DIR, "database.ini")
    params = config(filename=configuration_file, section="ost_reclamos_dev")
    df = pd.read_csv(csv_file)
    
    load_data_to_database(df)
