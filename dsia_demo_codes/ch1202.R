# treemap
library(treemapify)
library(ggplot2)
library(dplyr)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
pos <- df %>% 
  group_by(Pos) %>%
  summarise(freq = n())
ggplot(pos, aes(area = freq, label = Pos, fill = Pos)) +
  geom_treemap() +
  geom_treemap_text(fontface = "italic", colour = "white", place = "centre") +
  ggtitle("1995-1996 Chicago Bulls roster") +
  theme(legend.position = "none")