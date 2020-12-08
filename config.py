import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'server1149.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'zoo_db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin1149'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Pass1149'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'zoostorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '36ktu6YHeCGwfOT0jnLbcNLnMr4K3/FHfeqjGzeUJf44KP9fmxYt55l6a+dofYGI2L6fk+IsxAG0kurBTGd6mA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
