if (!require(RMySQL)) {
  install.packages("RMySQL")
}
if (!require(RMySQL)) {
  install.packages("bigrquery")
}
library(DBI)

con <- dbConnect(
  bigrquery::bigquery(),
  project = "datainpoint",
  dataset = "fav_nba_teams"
)

sql_statement <- "SELECT * FROM fav_nba_teams.boston_celtics WHERE number IN (34, 5, 20);"
gap <- dbGetQuery(con, statement = sql_statement)
View(gap)