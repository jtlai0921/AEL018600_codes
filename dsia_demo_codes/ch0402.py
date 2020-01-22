from pyquery import PyQuery as pq

def get_movie_rating(movie_url):
  rating_css = "strong span"               # 評分的 CSS 選擇器
  
  movie_doc = pq(movie_url)                # 取得網頁中所有的資料
  rating_elem = movie_doc(rating_css)      # 擷取評分資料
  movie_rating = float(rating_elem.text()) # 將標籤去除後轉換為浮點數
  return movie_rating

avenger_url = "https://www.imdb.com/title/tt4154756"
get_movie_rating(avenger_url)