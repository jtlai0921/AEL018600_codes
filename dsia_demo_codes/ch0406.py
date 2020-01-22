from pyquery import PyQuery as pq

def get_movie_cast(movie_url):
  cast_css = ".primary_photo+ td a"                                  # 演員名單的 CSS 選擇器
  
  movie_doc = pq(movie_url)                                          # 取得網頁中所有的資料
  cast_elem = movie_doc(cast_css)                                    # 擷取演員名單資料
  cast_genre = [x.text.replace("\n", "").strip() for x in cast_elem] # 將標籤去除
  return cast_genre

avenger_url = "https://www.imdb.com/title/tt4154756"
get_movie_cast(avenger_url)