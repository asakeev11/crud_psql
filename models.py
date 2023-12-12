import peewee

from psql import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Genre(BaseModel):
    genre_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'genres'


class Anime(BaseModel):
    anime_id = peewee.PrimaryKeyField(null=False)
    title = peewee.CharField(max_length=50)
    description = peewee.TextField()
    genre = peewee.ForeignKeyField(Genre, related_name='anime', to_field='genre_id', on_delete='cascade')

    class Meta:
        db_table = 'animes'


db.connect()
db.create_tables([Genre, Anime])


