library(rvest)
library(jsonlite)
library(dplyr)

get_nba_salary <- function() {
  nba_salary_ranking_url <- "https://www.spotrac.com/nba/rankings/"
  html_doc <- nba_salary_ranking_url %>% 
    read_html()
  player_css <- ".team-name"
  pos_css <- ".rank-position"
  salary_css <- ".info"
  players <- html_doc %>% 
    html_nodes(css = player_css) %>% 
    html_text()
  positions <- html_doc %>% 
    html_nodes(css = pos_css) %>% 
    html_text()
  salaries <- html_doc %>% 
    html_nodes(css = salary_css) %>% 
    html_text() %>% 
    gsub(pattern = "\\$", replacement = "", .) %>% 
    gsub(pattern = ",", replacement = "", .) %>% 
    as.numeric()
  #salaries <- gsub(pattern = "\\$", replacement = "", salaries)
  df <- data.frame(player = players,
                   pos = positions,
                   salary = salaries,
                   stringsAsFactors = FALSE)
  return(df)
}

get_pts_game <- function() {
  nba_stats_url <- "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS"
  res <- fromJSON(nba_stats_url)
  players <- res$resultSet$rowSet[, 3]
  pts_game <- as.numeric(res$resultSet$rowSet[, 23])
  df <- data.frame(player = players,
                   pts_game = pts_game,
                   stringsAsFactors = FALSE)
  return(df)
}

nba_salary <- get_nba_salary()
pts_game <- get_pts_game()
df <- merge(nba_salary, pts_game) %>% 
  arrange(desc(pts_game))
plot(df$pts_game, df$salary, type = "p")