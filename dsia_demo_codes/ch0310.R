if (!require(RMySQL)) {
  install.packages("RMySQL")
}
if (!require(RMySQL)) {
  install.packages("bigrquery")
}
library(DBI)
options("httr_oob_default" = TRUE)

csv_url <- "https://storage.googleapis.com/ds_data_import/boston_celtics_2007_2008.csv"
boston_celtics <- read.csv(csv_url, header = FALSE, skip = 1, col.names = c('number', 'player', 'pos', 'ht', 'wt', 'birth_date', 'college'))

con <- dbConnect(
  bigrquery::bigquery(),
  project = "datainpoint",
  dataset = "fav_nba_teams"
)
dbWriteTable(con, name = "boston_celtics", value = boston_celtics, overwrite = TRUE)