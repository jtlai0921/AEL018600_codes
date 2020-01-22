# read.csv() 使用預設參數
csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
csv_df <- read.csv(csv_url)
View(csv_df)