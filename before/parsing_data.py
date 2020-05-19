import pandas as pd
import requests
from datetime import datetime
headers = {'content-type': 'application/json'}

def parsing_movies():
    movies_data = open('movies.dat', 'r', encoding='ISO-8859-1')
    request_data_m = {'movies': []}
    for line in movies_data.readlines():
        [movieid, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        request_data_m['movies'].append({
            'movieid': movieid,
            'title': title,
            'genres': genres,
        })

def parsing_rating():
    rating_data = open('ratings.dat', 'r', encoding='ISO-8859-1')
    request_data_r = {'ratings': []}
    for line in rating_data.readlines():
        [userid, movieid, rate, timestamp] = line.split('::')
        timestamp = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        request_data_r['ratings'].append({
            'userid': userid,
            'movieid': movieid,
            'rate': rate,
            'time': timestamp
        })

def parsing_users():
    users_data = open('users.dat', 'r', encoding='ISO-8859-1')
    request_data_u = {'users':[]}
    for line in users_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        request_data_u['users'].append({
            'userid': userid,
            'gender': gender,
            'age': int(age),
            'occupation': occupation,
            'zipcode': zipcode
        })
        
if __name__ == '__main__':
    parsing_movies()
    parsing_rating()
    parsing_users()


data_1 = pd.merge(data_movies, data_rating, how = 'inner', on='movieid')
rating_movie_title = data_1.pivot(index= 'userid',
                                 columns = 'title',
                                 values = 'rate')
rating_movie_title.head(10)

data_2 = pd.merge(data_users, data_rating, how = 'inner', on='userid')
data_2 = data_2.drop('zipcode',axis=1)
data_2 = data_2.drop('time',axis=1)
data_2