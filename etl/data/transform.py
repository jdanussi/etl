# transform.py
""" Docstring """

import os
import pandas as pd
# from etl.constants import RESOURCES_DIR
from etl import RESOURCES_DIR  # porque existe __init__.py en etl/


def transform_data(df, csv_out):
    """ Docstring """

    # Drop "suspended" customers
    df["status_cli"] = df["status_cli"].str.lower()
    df.drop(df[df.status_cli == "s"].index, inplace=True)

    # Drop customer "Argensun"
    df.drop(df[df.cod_tit == "999999"].index, inplace=True)
    df["cod_tit"] = df["cod_tit"].astype(str)

    # Select a subset of columns
    cols = ["cod_tit", "razon_social"]
    df = pd.DataFrame(df, columns=cols)

    df["list_id"] = 10
    df["value"] = df["razon_social"].str.strip() + "   #" + df["cod_tit"].str.strip() + "#"

    df.rename(columns={"cod_tit": "extra"}, inplace=True)

    cols = ["list_id", "value", "extra"]
    df = df[cols]

    df.to_csv(csv_out, encoding="utf-8", index=False)
    return df


if __name__ == "__main__":

    csv_in = os.path.join(RESOURCES_DIR, "ct_clientes_raw.csv")
    csv_out = os.path.join(RESOURCES_DIR, "ct_clientes_transform.csv")
    df = pd.read_csv(csv_in)

    transform_data(df, csv_out)
