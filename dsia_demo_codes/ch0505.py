from selenium import webdriver
from random import randint
import time
from pyquery import PyQuery as pq

def get_movie_info(movie_url):
  """
  Get movie info from certain IMDB url
  """
  # 指定電影資訊的 CSS 選擇器
  rating_css = "strong span"
  genre_css = ".subtext a"
  poster_css = ".poster img"
  cast_css = ".primary_photo+ td a"
  
  movie_doc = pq(movie_url)
  # 擷取資訊
  rating_elem = movie_doc(rating_css)
  movie_rating = float(rating_elem.text())
  genre_elem = movie_doc(genre_css)
  movie_genre = [x.text.replace("\n", "").strip() for x in genre_elem]
  movie_genre.pop()
  movie_poster_elem = movie_doc(poster_css)
  movie_poster = movie_poster_elem.attr('src')
  movie_cast_elem = movie_doc(cast_css)
  movie_cast = [x.text.replace("\n", "").strip() for x in movie_cast_elem]
  
  # 回傳資訊
  movie_info = {
      "rating": movie_rating,
      "genre": movie_genre,
      "poster": movie_poster,
      "cast": movie_cast
  }
  return movie_info

def get_movies(*args):
  """
  Get multiple movies' info from movie titles
  """
  imdb_home = "https://www.imdb.com/"
  driver = webdriver.Firefox(executable_path="YOURGECKODRIVERPATH") # Use Firefox
  movies = dict()
  for movie_title in args:
    # 前往 IMDB 首頁
    driver.get(imdb_home)
    # 定位搜尋欄位
    search_elem = driver.find_element_by_css_selector("#navbar-query")
    # 輸入電影名稱
    search_elem.send_keys(movie_title)
    # 定位搜尋按鈕
    submit_elem = driver.find_element_by_css_selector("#navbar-submit-button .navbarSprite")
    # 按下搜尋按鈕
    submit_elem.click()
    # 定位搜尋結果連結
    first_result_elem = driver.find_element_by_css_selector("#findSubHeader+ .findSection .odd:nth-child(1) .result_text a")
    # 按下搜尋結果連結
    first_result_elem.click()
    # 呼叫 get_movie_info()
    current_url = driver.current_url
    movie_info = get_movie_info(current_url)
    movies[movie_title] = movie_info
    time.sleep(randint(3, 8))
  driver.close()
  return movies

movies = get_movies("Avengers: Infinity War", "Black Panther")
print(movies["Avengers: Infinity War"])
print(movies["Black Panther"])