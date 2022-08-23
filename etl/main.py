#main.py
import os
from etl.utils.db_config import config
from data.extract import get_data_from_database
from data.transform import transform_data
from data.load import load_data_to_database
from etl import UTILS_DIR, RESOURCES_DIR


def main():
    """ Docstring """

    configuration_file = os.path.join(UTILS_DIR, "database.ini")
    params = config(filename=configuration_file, section="Argensun-Prueba")
    csv_out_extract = os.path.join(RESOURCES_DIR, "ct_clientes_raw.csv")
    csv_out_transform = os.path.join(RESOURCES_DIR, "ct_clientes_transform.csv")
    
    df = transform_data(get_data_from_database(params, csv_out_extract), csv_out_transform)
    return df


if __name__ == "__main__":
    df = main()
    print(df)