csv_url <- "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df <- read.csv(csv_url, stringsAsFactors = FALSE)
df %>% 
  arrange(year) %>%       # 依照 year 遞增排序
  head()

df %>%
  arrange(desc(year)) %>% # 依照 year 遞減排序
  head()