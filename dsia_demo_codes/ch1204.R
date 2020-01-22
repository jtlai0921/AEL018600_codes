library(dplyr)
library(ggplot2)

per_game_url <- "https://storage.googleapis.com/ds_data_import/stats_per_game_chicago_bulls_1995_1996.csv"
player_info_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
per_game <- read.csv(per_game_url)
player_info <- read.csv(player_info_url)
df <- merge(player_info, per_game[, c("Name", "PTS.G")], by.x = "Player", by.y = "Name")
df %>% 
  group_by(Pos) %>% 
  summarise(mean_pts = mean(PTS.G)) %>%
  arrange(mean_pts) %>% 
  mutate(x = 1:5) %>% 
  ggplot(aes(x=x, y=mean_pts)) +
  geom_segment(aes(x=x, xend=x, y=0, yend=mean_pts), color="grey") +
  geom_point(color="orange", size=4) +
  geom_text(aes(label = sprintf("%.1f", mean_pts), y= mean_pts),  hjust = -1) +
  theme_light() +
  scale_x_continuous(breaks = 1:5, labels = c("PF", "C", "PG", "SF", "SG")) +
  scale_y_continuous(limits = c(0, 35)) +
  coord_flip() +
  theme(
    panel.grid.major.x = element_blank(),
    panel.border = element_blank(),
    axis.ticks.x = element_blank()
  ) +
  ggtitle("1995-1996 Chicago Bulls PPG by positions") +
  xlab("") +
  ylab("")