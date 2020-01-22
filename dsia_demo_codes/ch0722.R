csv_url <- "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df <- read.csv(csv_url, stringsAsFactors = FALSE)
df %>% 
  arrange(year, desc(continent)) %>%  # 先依照 year 遞增排序再依照 continent 遞減排序
  head()