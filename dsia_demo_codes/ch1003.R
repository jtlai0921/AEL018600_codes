library(dplyr)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
pos <- df %>% 
  group_by(Pos) %>%
  summarise(freq = n())
barplot(pos$freq, names.arg = pos$Pos)