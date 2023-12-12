from models import Anime, Genre


# def delete_anime():
#     for i in Anime.select():
#         print(i.anime_id, '---', i.title)
#     choice = int(input('Select ID: '))
#     del_anime = Anime.get(anime_id=choice)
#     del_anime.delete_instance()
#     print(f'Deleted: {del_anime.title}')
#
#
# delete_anime()

# query = Anime.delete().where(Anime.genre == 1)
# query.execute()
