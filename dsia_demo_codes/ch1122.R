library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
labs <- c("Center", "Power Forward", "Point Guard", "Small Forward", "Shooting Guard")
df %>% 
  ggplot(aes(x = Pos, fill = Pos)) +
  geom_bar(alpha = 0.7) +
  ggtitle("Front court players are the majorities.") +
  labs(subtitle = "Chicago Bulls is relatively weak in the paint.",
       caption = "Source: basketball-reference.com") +
  xlab("Positions") +
  ylab("Number of Players") +
  scale_x_discrete(labels = labs) +
  scale_y_continuous(breaks = 1:4) +
  theme(legend.position = "none") # 移除圖例