# main.py
""" Docstring """

import os
from etl import get_data_from_database, transform_data, load_data_to_database
from etl import config
from etl import RESOURCES_DIR, CONFIGURATION_FILE


def main():
    """Docstring"""

    params_source = config(filename=CONFIGURATION_FILE, section="database1")
    params_destination = config(filename=CONFIGURATION_FILE, section="database2")

    csv_out_extract = os.path.join(RESOURCES_DIR, "csv_raw.csv")
    csv_out_transform = os.path.join(RESOURCES_DIR, "csv_transform.csv")

    load_data_to_database(
        params_destination,
        transform_data(
            get_data_from_database(params_source, csv_out_extract), csv_out_transform
        ),
    )


if __name__ == "__main__":
    main()
