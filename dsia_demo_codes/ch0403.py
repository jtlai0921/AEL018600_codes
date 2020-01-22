from pyquery import PyQuery as pq

def get_movie_genre(movie_url):
  genre_css = ".subtext a"                                             # 電影類型的 CSS 選擇器
  
  movie_doc = pq(movie_url)                                            # 取得網頁中所有的資料
  genre_elem = movie_doc(genre_css)                                    # 擷取評分資料
  movie_genre = [x.text.replace("\n", "").strip() for x in genre_elem] # 將標籤去除
  movie_genre.pop()                                                    # 將最後一個元素上映日期拋出
  return movie_genre

avenger_url = "https://www.imdb.com/title/tt4154756"
get_movie_genre(avenger_url)