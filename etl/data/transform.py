# transform.py
""" Docstring """

import pandas as pd


def transform_data(dframe, csv_file):
    """Docstring"""

    # Drop "suspended" customers
    dframe["status_cli"] = dframe["status_cli"].str.lower()
    dframe.drop(dframe[dframe.status_cli == "s"].index, inplace=True)

    # Drop customer "Argensun"
    dframe.drop(dframe[dframe.cod_tit == "999999"].index, inplace=True)
    dframe["cod_tit"] = dframe["cod_tit"].astype(str)

    # Select a subset of columns
    cols = ["cod_tit", "razon_social"]
    dframe = pd.DataFrame(dframe, columns=cols)

    dframe["list_id"] = 10
    dframe["value"] = (
        dframe["razon_social"].str.strip()
        + "   #"
        + dframe["cod_tit"].str.strip()
        + "#"
    )

    dframe.rename(columns={"cod_tit": "extra"}, inplace=True)

    cols = ["list_id", "value", "extra"]
    dframe = dframe[cols]

    dframe.to_csv(csv_file, encoding="utf-8", index=False)
    return dframe
