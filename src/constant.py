import os


def _join_abspath(*args):
    return os.path.abspath(os.path.join(*args))


PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PATH_TO_PROJECT_DIR = _join_abspath(PATH_TO_THIS_DIR, '..')

PATH_TO_SQL = _join_abspath(PATH_TO_PROJECT_DIR, 'sql')
PATH_TO_SQL_BIGQUERY = _join_abspath(PATH_TO_SQL, 'bigquery')
PATH_TO_SQL_MYSQL = _join_abspath(PATH_TO_SQL, 'mysql')
# credential
PATH_TO_CREDENTIAL = _join_abspath(PATH_TO_PROJECT_DIR, 'credential')
# data
PATH_TO_DATA = _join_abspath(PATH_TO_PROJECT_DIR, 'data')
PATH_TO_DATA_RAW = _join_abspath(PATH_TO_DATA, 'raw')
PATH_TO_DATA_PROCESSED = _join_abspath(PATH_TO_DATA, 'processed')
