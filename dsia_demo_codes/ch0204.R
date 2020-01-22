# read.csv() 自行指定變數的名稱
csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
csv_df <- read.csv(csv_url, skip = 1, header = FALSE, col.names = c('number', 'player', 'pos', 'ht', 'wt', 'birth_date', 'college'))
View(csv_df)