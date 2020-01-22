library(rvest)
library(tidyr)
library(ggplot2)

get_pp_stats <- function() {
  stats_url <- "https://www.basketball-reference.com/players/p/piercpa01.html"
  html_doc <- stats_url %>% 
    read_html()
  pts_css <- "#per_game .full_table .right:nth-child(30)"
  ast_css <- "#per_game .full_table .right:nth-child(25)"
  reb_css <- "#per_game .full_table .right:nth-child(24)"
  pts <- html_doc %>% 
    html_nodes(pts_css) %>% 
    html_text() %>% 
    as.numeric()
  ast <- html_doc %>% 
    html_nodes(ast_css) %>% 
    html_text() %>% 
    as.numeric()
  reb <- html_doc %>% 
    html_nodes(reb_css) %>% 
    html_text() %>% 
    as.numeric()
  year <- paste(1999:2017, "01", "01", sep = "-") %>% 
    as.Date()
  df <- data.frame(year = year,
                   pts = pts,
                   ast = ast,
                   reb = reb,
                   stringsAsFactors = FALSE)
  return(df)
}

pp_stats <- get_pp_stats()
pp_stats_long <- gather(pp_stats, key = "stats", value = "value", pts, ast, reb)
ggplot(pp_stats_long, aes(x = year, y = value, color = stats)) +
  geom_line()