import peewee

db = peewee.PostgresqlDatabase(
    'test_start',
    user='talgat',
    password='1',
    host='localhost',
    port=5432
)
