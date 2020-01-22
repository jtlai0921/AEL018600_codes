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

avenger_url = "https://www.imdb.com/title/tt4154756"
get_movie_info(avenger_url)