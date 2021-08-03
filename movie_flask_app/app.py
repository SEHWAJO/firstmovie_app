from os import name
from flask import Flask, request, render_template, request, jsonify, redirect, url_for
import movie_sun
import requests
import json
import pandas as pd
import psycopg2
import csv, sqlite3
import datetime


def create_app():

    # 앱 생성
    app = Flask(__name__)

    # url 라우터(메인화면)
    @app.route('/')
    def index():
        return render_template('index.html')


    # url 라우터(가장 인기있는 영화 17개 보여주기)
    @app.route('/top17')
    def top17():
        info = movie_sun.select_all()
        retstr = ''
        for i, v in enumerate(info):
            retstr += '%d. Title: %s <br> Popularity: %s <br> Release_date: %s <br> Rate: %s <br><br><br><br>' % (i+1, v[9], v[6], v[8], v[12])
        return retstr


    # 라우터(영화제목으로 영화 정보 찾기 - 첫 화면)
    @app.route('/findmovie', methods=['get'])
    def findmovie():
        if request.method == 'get':
            
            title= request.args.get('title')
            return render_template("findmovie.html")
        
        return render_template("findmovie.html")

    # 라우터(영화제목으로 영화 정보 찾기 - 검색 누르면 넘어가는 화면)
    @app.route('/searchtitle')
    def searchtitle():
        
        # first_movie = first_movie[0]
        title= request.args.get('title') # 중요!
        
        URL_serch = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key=f36b3b9b841d7e2e969763cce0adc79a"
        search_data = requests.get(URL_serch)
        movies_search = json.loads(search_data.text) # 문자열을 딕셔너리 형태로 바꿔줌 - 접근 가능하도록

        first_movie = movies_search["results"] # 맨위의 영화 정보만 추출
        first_movie = first_movie[0]
        first_movie = 'Title: %s <br><br> Overview: %s <br><br> Popularity: %s <br><br> Release_date: %s <br><br> Rate: %s <br><br>' % (first_movie['title'], first_movie['overview'], first_movie['popularity'], first_movie['release_date'], first_movie['vote_average'])
        return first_movie#render_template('findmovie.html', data = first_movie)
        

    # 라우터 (note 영화리뷰노트 - 첫 화면)
    @app.route('/note', methods=["get", "post"])
    def note():
        # return render_template('review.html')

        if request.method == 'GET': 
            # return "get"
        # args_dict = request.args.to_dict() 
        # print(args_dict) 
            title2 = request.args.get("title2") 
            director = request.args.get("director")
            # return "get"
            return render_template("review.html")
        else: 
            # return "post"
            title2 = request.form("title2")
            director = request.form("director")
            return render_template("review.html")


    @app.route('/notesave') # 리뷰작성완료 누르면 넘어가는 화면인데 작동 안함
    def notesave():
        title2 = request.args.get("title2") 
        director = request.args.get("director")
            # return "get"
        return 'get 이다. 영화제목: {} 메모: {}'.format(title2, director) 
        # else: 
        #     # return "post"
        #     title2 = request.form("title2")
        #     director = request.form("director")
        #     return 'POST 이다. 영화제목: {} 메모: {}'.format(title2, director) 



    @app.route('/method', methods=['GET', 'POST']) 
    def method(): 
        if request.method == 'GET': 
            return 'GET 으로 전송이다.' 
        else: 
            title = request.form("title") 
            note = request.form("note")
            movie_sun.insert_data(title, note) 
            return 'POST 이다. 영화제목: {} 메모: {}'.format(title, note) 


    # url 라우터(카카오톡 로그인)
    @app.route('/signin')
    def kakaoLogin():
        return render_template('kakaoLogin.html')


    # @app.route('/search', methods=['GET', 'POST']) 
    # def search(): 
    #     if request.method == 'GET': 
    #         args_dict = request.args.to_dict() 
    #         print(args_dict) 
    #         title_name = request.args.get["title_name"] 
    #         return "GET으로 전달된 데이터({})".format(title_name) 
    #     else: 
    #         title_name = request.form["title_name"]
    #         with open("static/save.txt","w", encoding='utf-8') as f: 
    #             f.write("%s,%s" % (title_name)) 
    #         return "POST로 전달된 데이터({})".format(title_name)



    # @app.route('/memo', methods=['GET']) 
    # def listing(): 
    #     sample_receive = request.args.get('sample_give') 
    #     print(sample_receive) 
    #     return jsonify({'msg':'GET 연결되었습니다!'}) 

    # ## API 역할을 하는 부분 
    # @app.route('/memo', methods=['POST']) 
    # def saving(): 
    #     sample_receive = request.form['sample_give'] 
    #     print(sample_receive) 
    #     return jsonify({'msg':'POST 연결되었습니다!'}) 
        
    # if __name__ == '__main__': 
    #     app.run('0.0.0.0',port=5000,debug=True)



    # 메인 영역
    if __name__ == "__main__":
        app.run(debug=True)
    
    return app




