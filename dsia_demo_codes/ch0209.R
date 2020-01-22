# readxl::read_excel() 函數使用預設參數
if (!require(readxl)) {
  install.packages("readxl")
  library(readxl)
}

xlsx_url <- "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
dest_file <- "~/Desktop/fav_nab_teams.xlsx"
download.file(xlsx_url, destfile = dest_file)
chicago_bulls <- read_excel(dest_file)
View(chicago_bulls)