# utils/db_config.py
""" Docstring """

from configparser import ConfigParser


def config(filename="database.ini", section="foo"):
    """
    Configures connection to PostgreSQL database instance
    :rtype: object
    :param filename: database configuration file path
    :param section: section of database configuration file to use
    :return: db connection
    """
    # create a parser
    parser = ConfigParser()
    # read database configuration file
    parser.read(filename)

    # get section of database configuration file
    database = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]
    else:
        raise Exception(
            # "Section {0} not found in the {1} file".format(section, filename)
            f"Section {section} not found in the {filename} file"
        )
    return database
