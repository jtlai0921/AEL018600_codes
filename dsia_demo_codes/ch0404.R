# install.packages(c("rvest", "magrittr"))
library(rvest)
library(magrittr) # 使用 %>% 運算子

get_movie_rating <- function(movie_url) {
  rating_css <- "strong span"
  rating_xpath <- "//strong/span"
  
  movie_rating <- movie_url %>% 
    read_html() %>%                        # 取得網頁中所有的資料
    html_nodes(css = rating_css) %>%       # 擷取評分資料
    # html_nodes(xpath = rating_xpath) %>% # 亦可以使用 XPath 擷取評分資料
    html_text() %>%                        # 去除 html 標籤
    as.numeric()                           # 轉換為浮點數
  
  return(movie_rating)
}

avenger_url <- "https://www.imdb.com/title/tt4154756"
get_movie_rating(avenger_url)