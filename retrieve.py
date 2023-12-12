import peewee
from models import Genre, Anime, db


def retrieve_anime():
    query = Anime.select(Anime.anime_id, Anime.title, Anime.description, Anime.genre)
    print(*[f'{(i.anime_id, i.title)}\n' for i in query])
    choice = int(input('Choose anime ID: '))
    for anime in query:
        if choice == anime.anime_id:
            print(f'ID: {anime.anime_id}\nTitle: {anime.title}\nDescription: {anime.description}\nGenre: '
                  f'{anime.genre}')


# retrieve_anime()


def retrieve_genre():
    genre = Genre.select()
    for i in genre:
        print(f'{i.genre_id} --- {i.name}')
    choice = int(input('Select the genre: '))
    query = Anime.select(Anime.anime_id, Anime.title, Anime.description).where(Anime.genre == choice)
    for i in genre:
        if i.genre_id == choice:
            print(' '*20, i.name.capitalize())
    for i in query:
        print(f'ID: {i.anime_id},  Title: {i.title},  Desc: {i.description}')


# retrieve_genre()
#select title, description, name as genre from animes join genres on animes.genre_id=genres.genre_id;
def alter_retrieve_genre():
    query = ('SELECT anime_id, title, description, name AS genre FROM animes JOIN genres ON animes.genre_id = '
             'genres.genre_id;')
    res = db.execute_sql(query)
    genres = Genre.select(Genre.name)
    for i in genres:
        print(i.name)
    choice = input('Select the genre: ')
    print(' ' * 20, choice.capitalize())
    for row in res:
        if choice == row[3]:
            print(f'ID: {row[0]},  Title: {row[1]},  Desc: {row[2]},  Genre: {row[3]}')


# alter_retrieve_genre()

def main():
    choice = int(input('Select: \n1)retrieve_anime\n2)retrieve_genre\n3)alter_retrieve_genre: '))
    if choice == 1:
        retrieve_anime()
    elif choice == 2:
        retrieve_genre()
    elif choice == 3:
        alter_retrieve_genre()
    else:
        print('Invalid choice')
        main()

    ask = input('Хотите продолжить\'?(YES/NO)\n\t')
    if ask.lower() == 'yes':
        main()
    else:
        print('Bye!')


main()
