csv_url <- "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df <- read.csv(csv_url, stringsAsFactors = FALSE)
View(df)