import peewee

from models import Anime

# a = Anime.get(anime_id=1)


def update_anime():
    for i in Anime.select():
        print(f'{i.anime_id} --- {i.title}')
    choice = int(input('Select anime by ID: '))
    choose_action = input('Choose an action: Title, description, genre: ').lower()
    for i in Anime.select():
        try:
            if choice == i.anime_id:
                if choose_action == 'title':
                    new_title = input('New title: ')
                    query = Anime.update(title=new_title).where(Anime.anime_id == choice)
                    query.execute()
                elif choose_action == 'description':
                    new_desc = input('New desc: ')
                    query = Anime.update(description=new_desc).where(Anime.anime_id == choice)
                    query.execute()
                elif choose_action == 'genre':
                    new_genre = int(input('New genre ID: '))
                    query = Anime.update(genre_id=new_genre).where(Anime.anime_id == choice)
                    query.execute()
                else:
                    print('Wrong choice')
        except ValueError:
            print('Wrong choice')
    for anime in Anime.select():
        print(anime.anime_id, anime.title, anime.description, anime.genre_id)


update_anime()