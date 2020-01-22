# install.packages(c("rvest", "magrittr"))
library(rvest)
library(magrittr) # 使用 %>% 運算子

get_movie_genre <- function(movie_url) {
  genre_css <- ".subtext a"
  genre_xpath <- "//div[@class='subtext']/a"
  
  movie_genre <- movie_url %>% 
    read_html() %>%                             # 取得網頁中所有的資料
    html_nodes(xpath = genre_xpath) %>%         # 使用 XPath 擷取評分資料
    # html_nodes(css = genre_css) %>%           # 亦可以使用 CSS 選擇器擷取評分資料
    html_text()                                 # 去除 html 標籤
  movie_genre_len <- length(movie_genre)
  movie_genre <- movie_genre %>%
    `[` (-movie_genre_len) %>%                  # 將最後一個元素上映日期刪去
    gsub(pattern = "\n", replacement = "") %>%  # 去除換行符號
    trimws(which = "both")                      # 去除前後空白
  
  return(movie_genre)
}

avenger_url <- "https://www.imdb.com/title/tt4154756"
get_movie_genre(avenger_url)