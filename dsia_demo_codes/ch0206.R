# read.table() 指定 sep = ";"
txt_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.txt"
txt_df <- read.table(txt_url, sep = ";", header = TRUE)
View(txt_df)