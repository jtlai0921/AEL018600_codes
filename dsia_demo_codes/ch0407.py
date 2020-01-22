from pyquery import PyQuery as pq

def get_movie_poster(movie_url):
  poster_css = ".poster img"          # 電影海報的 CSS 選擇器
  
  movie_doc = pq(movie_url)           # 取得網頁中所有的資料
  poster_elem = movie_doc(poster_css) # 擷取電影海報資料
  poster = poster_elem.attr('src')    # 將標籤去除，保留連結
  return poster

avenger_url = "https://www.imdb.com/title/tt4154756"
get_movie_poster(avenger_url)