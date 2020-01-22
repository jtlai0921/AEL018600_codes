# Error: stat_count() must not be used with a y aesthetic.
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
  ggplot(aes(x = Pos, y = mean_pts)) +
    geom_bar()