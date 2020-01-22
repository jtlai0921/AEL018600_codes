library(rvest)
library(ggplot2)

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
  df <- data.frame(player = players,
                   pos = positions,
                   salary = salaries,
                   stringsAsFactors = FALSE)
  return(df)
}
nba_salary <- get_nba_salary()
nba_salary %>% 
  ggplot(aes(x = salary, colour=pos, fill=pos)) +
    geom_density(alpha = 0.5) +
    ggtitle("Salary of NBA players by positions") +
    facet_wrap(~pos) +
    theme(legend.position = "none")