library(dplyr)
library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
df %>% 
  ggplot(aes(x = Pos)) +
    geom_bar()