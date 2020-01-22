# readxl::read_excel() 函數指定工作表與讀取範圍
if (!require(readxl)) {
  install.packages("readxl")
  library(readxl)
}

xlsx_url <- "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
dest_file <- "~/Desktop/fav_nab_teams.xlsx"
download.file(xlsx_url, destfile = dest_file)
boston_celtics <- read_excel(dest_file, sheet = "boston_celtics_2007_2008", range = "A7:C16", col_names = c("number", "player", "pos"))
View(boston_celtics)