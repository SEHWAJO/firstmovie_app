import requests
import json
import pandas as pd
import psycopg2
import csv, sqlite3
import datetime

# 메인 페이지 (가장 인기있는 영화 보여주기)
URL_pop = "https://api.themoviedb.org/3/movie/popular?api_key=f36b3b9b841d7e2e969763cce0adc79a"
pop_data = requests.get(URL_pop)
movies_pop = json.loads(pop_data.text) # 문자열을 딕셔너리 형태로 바꿔줌 - 접근 가능하도록


results = movies_pop['results'] # 키값이 results 인 values만 추출


movie_keys = [] # 키값 확인용
movie_values = []


for movie in results:
   
    #movie_keys = movie.keys() 
    #keys_df = pd.DataFrame(movies_key)
    movie_values.append(list(movie.values()))
    #### movie_values = movie_values.pop(2)
     #values_df = pd.DataFrame(movies_values)


for movie_value in movie_values:
    movie_value.pop(2)
    


# conn = psycopg2.connect(
#     host="satao.db.elephantsql.com", # 서버 호스트 주소
#     database="jmrhavhw", # 데이터베이스 이름
#     user="jmrhavhw", # 유저 이름
#     password="hTnJ15Kka4UtnYzK6k8W43xoRWLkteVb") # 유저 비밀번호

# cur = conn.cursor()

# cur.execute("CREATE TABLE movie_title (title varchar(50), note varchar(200))")
# conn.commit() 



"""
cur.execute("CREATE TABLE Popular_Movie(adult bool, backdrop_path VARCHAR(50), id VARCHAR(50), original_language VARCHAR(50), original_title VARCHAR(100), overview VARCHAR(1000), popularity float, poster_path VARCHAR(50), release_date VARCHAR(50), title VARCHAR(50), video VARCHAR(50), vote_average float, vote_count float)")
conn.commit()



test0 = [movie_values[0]]
test1 = [movie_values[1]]
test2 = [movie_values[2]]
test3 = [movie_values[3]]
test4 = [movie_values[4]]
test5 = [movie_values[5]]
test6 = [movie_values[6]]
test7 = [movie_values[7]]
test8 = [movie_values[8]]
test9 = [movie_values[9]]
test10 = [movie_values[10]]
test11 = [movie_values[11]]
test12 = [movie_values[12]]
test13 = [movie_values[13]]
test14 = [movie_values[14]]
test15 = [movie_values[15]]
test16 = [movie_values[16]]
test17 = [movie_values[17]]
test18 = [movie_values[18]]
test19 = [movie_values[19]]

cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test0)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test1)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test2)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test3)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test4)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test5)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test6)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test7)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test8)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test9)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test10)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test11)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test12)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test13)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test14)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test15)
cur.executemany("INSERT INTO Popular_Movie VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test16)
# cur.executemany("INSERT INTO Popular_Movie10 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test17)
# cur.executemany("INSERT INTO Popular_Movie10 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test18)
# cur.executemany("INSERT INTO Popular_Movie10 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", test19)
conn.commit()
conn.close()

"""


# db 연결 함수 만들기(psycopg2로 연결)

def dbcon():
    return psycopg2.connect(
    host="satao.db.elephantsql.com", # 서버 호스트 주소
    database="jmrhavhw", # 데이터베이스 이름
    user="jmrhavhw", # 유저 이름
    password="hTnJ15Kka4UtnYzK6k8W43xoRWLkteVb") # 유저 비밀번호



def select_all():
    ret = list()
    try:    
        conn = dbcon()
        cur = conn.cursor()
        cur.execute('SELECT * FROM popular_movie')
        ret = cur.fetchall()
    except Exception as e:
        print('db error', e)
    finally:
        conn.close()
        return ret




def select_title(title):
    ret = ()
    try:    
        conn = dbcon()
        cur = conn.cursor()
        setdata = (title,)
        cur.execute('SELECT * FROM popular_movie WHERE title = ?', setdata)
        ret = cur.fetchone()
    except Exception as e:
        print('db error', e)
    finally:
        conn.close()
        return ret










from flask import Flask, render_template, jsonify, request, redirect, url_for, abort



app = Flask(__name__) 

import requests 
from bs4 import BeautifulSoup 

import requests
import json
import pandas as pd
import psycopg2
import csv, sqlite3
import datetime







# 데이터 넣는 함수
def insert_data(title, note): 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (title, note) 
        c.execute("INSERT INTO student VALUES (?, ?)", setdata) 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: db.close()




def select_all2():
    ret = list()
    try:    
        conn = dbcon()
        cur = conn.cursor()
        cur.execute('SELECT * FROM movie_title')
        ret = cur.fetchall()
    except Exception as e:
        print('db error', e)
    finally:
        conn.close()
        return ret





# 타이틀로 영화 검색하기

def select_title(title):
    URL_serch = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key=f36b3b9b841d7e2e969763cce0adc79a"
    search_data = requests.get(URL_serch)
    movies_search = json.loads(search_data.text) # 문자열을 딕셔너리 형태로 바꿔줌 - 접근 가능하도록

    first_movie = movies_search["results"] # 맨위의 영화 정보만 추출
    first_movie = first_movie[0]


    return first_movie






# def select_title(title):
#     ret = ()
#     try:    
#         conn = dbcon()
#         cur = conn.cursor()
#         setdata = (title,)
#         cur.execute('SELECT * FROM popular_movie WHERE title = ?', setdata)
#         ret = cur.fetchone()
#     except Exception as e:
#         print('db error', e)
#     finally:
#         conn.close()
#         return ret







# @app.route('/review', methods=['POST']) 
# def write_review(): 
#     title_receive = request.form['title_give'] 
#     author_receive = request.form['author_give'] 
#     review_receive = request.form['review_give'] 
#     put_db = { 
#         'title' : title_receive, 
#         'author' : author_receive, 
#         'review' : review_receive 
#         } 
#         conn.bookreview.insert_one(put_db)
#         # conn.commit()
#         return jsonify({'msg': '저장완료'})







