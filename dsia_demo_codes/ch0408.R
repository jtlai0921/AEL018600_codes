# install.packages(c("rvest", "magrittr"))
library(rvest)
library(magrittr) # 使用 %>% 運算子

get_movie_cast <- function(movie_url) {
  cast_css <- ".primary_photo+ td a"
  cast_xpath <- "//td[2]/a"
  
  movie_cast <- movie_url %>% 
    read_html() %>%                             # 取得網頁中所有的資料
    html_nodes(xpath = cast_xpath) %>%          # 使用 XPath 擷取演員名單
    # html_nodes(css = cast_css) %>%            # 亦可以使用 CSS 選擇器擷取演員名單
    html_text() %>%                             # 去除 html 標籤
    gsub(pattern = "\n", replacement = "") %>%  # 去除換行符號
    trimws(which = "both")                      # 去除前後空白
  return(movie_cast)
}

avenger_url <- "https://www.imdb.com/title/tt4154756"
get_movie_cast(avenger_url)