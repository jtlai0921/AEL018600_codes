library(rvest)
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
avg_pts <- mean(pp_stats$pts)
pp_stats %>% 
  ggplot(aes(x = year, y = pts)) +
    geom_line() +
    ggtitle("Points per game: Paul Pierce in Boston") +
    # 調整 X 軸的範圍與樣式
    scale_x_date(date_breaks = "1 year", date_labels = "%Y", limits = c(as.Date("1999-01-01"), as.Date("2013-01-01"))) +
    # 調整 Y 軸的範圍
    scale_y_continuous(limits = c(15, 30)) +
    xlab("Year") +
    ylab("PPG")