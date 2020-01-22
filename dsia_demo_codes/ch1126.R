library(rvest)
library(ggplot2)

# Get NBA players' salary data from ESPN.com
get_nba_salary_data <- function() {
  salary_urls <- sprintf("http://www.espn.com/nba/salaries/_/page/%s/seasontype/4", 1:9)
  players <- c()
  positions <- c()
  salaries <- c()
  for (salary_url in salary_urls) {
    player_pos_css <- ".evenrow td:nth-child(2) , .oddrow td:nth-child(2)"
    salary_css <- ".evenrow td:nth-child(4) , .oddrow td:nth-child(4)"
    player_pos <- salary_url %>% 
      read_html() %>% 
      html_nodes(player_pos_css) %>% 
      html_text()
    player_pos_split <- player_pos %>% 
      strsplit(split = ", ")
    player <- c()
    position <- c()
    for (i in 1:length(player_pos_split)) {
      player <- c(player, player_pos_split[[i]][1])
      position <- c(position, player_pos_split[[i]][2])
    }
    salary <- salary_url %>% 
      read_html() %>% 
      html_nodes(salary_css) %>% 
      html_text() %>% 
      gsub(pattern = "\\$", replacement = "") %>% 
      gsub(pattern = ",", replacement = "") %>% 
      as.numeric()
    positions <- c(positions, position)
    players <- c(players, player)
    salaries <- c(salaries, salary)
  }
  df <- data.frame(player = players, position = positions, salary = salaries, stringsAsFactors = FALSE)
  return(df)
}

df <- get_nba_salary_data()
ggplot(df, aes(x = salary, color = position)) +
  geom_histogram(alpha = 0.7, bins = 15)

ggplot(df, aes(x = salary, color = position)) +
  geom_freqpoly(alpha = 0.7, bins = 15)