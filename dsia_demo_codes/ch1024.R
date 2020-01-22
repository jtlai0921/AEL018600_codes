library(rvest)

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
plot(pp_stats$year, pp_stats$pts, type = "l", lwd = 3, col = rgb(1, 0, 0, 0.5),
     ylim = c(min(pp_stats$ast), max(pp_stats$pts)))
lines(pp_stats$year, pp_stats$reb, lwd = 3, col = rgb(0, 1, 0, 0.5))
lines(pp_stats$year, pp_stats$ast, lwd = 3, col = rgb(0, 0, 1, 0.5))
legend("topright", legend=c("PTS", "REB", "AST"), cex = 0.5, bty = "n",
       col = c("red", "green", "blue"), lty = c(1, 1, 1))