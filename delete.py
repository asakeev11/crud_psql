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

# first_name, last_name, *some, age = ['John', 'Green', 'USA', 'CEO', 'Ferrari', '3 Kids', '45yo']
# print(first_name, last_name, some, age)

# *_, = range(5)
# print(_)
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
#
# print(factorial(501))
