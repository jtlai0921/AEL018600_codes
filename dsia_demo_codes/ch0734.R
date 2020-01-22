library(dplyr)

csv_url <- "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df <- read.csv(csv_url, stringsAsFactors = FALSE)
df %>% 
  filter(year == 2007) %>% 
  group_by(continent) %>% 
  summarise(ttl_pop = sum(as.numeric(pop))) # integer 會溢位，轉換為 numeric