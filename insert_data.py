import peewee
from models import Genre, Anime


def add_genre(name):
    try:
        genre = Genre(name=name.lower().strip())
        genre.save()
        print(f'Genre created: {name.strip()}')
    except (peewee.IntegrityError, peewee.InternalError):
        raise RuntimeError('Genre already exists')


# add_genre('Sport')


def add_anime(title, description, genre):
    try:
        genre = Genre.select().where(Genre.name == genre.lower().strip()).get()
        genre_exist = True
    except peewee.DoesNotExist:
        raise RuntimeError('Genre does not exist')
    try:
        if genre_exist:
            anime = Anime(
                title=title,
                description=description,
                genre=genre
            )

            anime.save()
            print('Anime added')
        else:
            print(f'Genre {genre} does not exist')
    except (peewee.IntegrityError, peewee.InternalError):
        raise RuntimeError('This anime is already added')


# add_anime('Ping pong', 'Anime about football', 'Sport')





# print(find_animes())
# animes = find_animes()
# for i in animes:
#     print(f"ID: {i.anime_id}, Title: {i.title}, Genre: {i.genre_id}" )
# choice = int(input('ID of anime: '))
# for i in animes:
#     if i.anime_id == choice:
#         print(i.title)

genre = Genre.get(name='sport')
print(genre.anime)