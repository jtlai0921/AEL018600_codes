library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
df %>% 
  ggplot(aes(x = Pos)) +
  geom_bar(fill = "red", alpha = 0.5) +
  ggtitle("Front court players are the majorities.") +
  labs(subtitle = "Chicago Bulls is relatively weak in the paint.",
       caption = "Source: basketball-reference.com") +
  xlab("Positions") +
  ylab("Number of Players")