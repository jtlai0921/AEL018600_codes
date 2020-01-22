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
    geom_hline(yintercept = avg_pts, lty = 2, col = "green") +
    geom_ribbon(aes(ymin = avg_pts, ymax = pts, 
                fill = ifelse(pts >= avg_pts, TRUE, NA)),
                alpha = 0.5) +
    # 增加註釋文字
    annotate("text", x = as.Date("2013-01-01"), y = 25, label = "Left Boston Celtics") +
    # 增加箭頭
    geom_segment(aes(x = as.Date("2013-01-01"), y = 23, xend = as.Date("2013-01-01"), yend = 20),
                 arrow = arrow(length = unit(0.2, "cm"))) +
    scale_fill_manual(values=c("gray"), name="fill") +
    theme(legend.position="none") +
    ggtitle("Points per game: Paul Pierce") +
    xlab("Year") +
    ylab("PPG")