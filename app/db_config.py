import peewee
from decouple import config

psql_db = peewee.PostgresqlDatabase(
        database=config("DB"),
        user=config("USER"),
        password=config("PASSWORD"),
        host=config("HOST"),
        port=5432
    )
# psql_db.connect()
