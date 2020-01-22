if (!require(rvest)) {
  install.packages("rvest")
}
if (!require(magrittr)) {
  install.packages("magrittr")
}

library(rvest)
library(magrittr) # 使用 %>% 運算子

avenger_url <- "https://www.imdb.com/title/tt4154756"
get_movie_cast(avenger_url)

get_movie_poster <- function(movie_url) {
  poster_css <- ".poster img"
  
  movie_poster <- movie_url %>% 
    read_html() %>%                  # 取得網頁中所有的資料
    html_nodes(css = poster_css) %>% # 使用 CSS 選擇器擷取電影海報連結
    html_attr("src")                 # 去除 html 標籤
  
  return(movie_poster)
}

avenger_url <- "https://www.imdb.com/title/tt4154756"
get_movie_poster(avenger_url)