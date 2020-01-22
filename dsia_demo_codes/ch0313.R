# install.packages(c("bigrquery", "RMySQL"))
library(DBI)

con <- dbConnect(
  bigrquery::bigquery(),
  project = "datainpoint",
  dataset = "fav_nba_teams"
)

boston_celtics <- dbReadTable(con, name = 'boston_celtics')
View(boston_celtics)