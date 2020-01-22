# jsonlite::fromJSON() 函數載入 JSON 檔案
if (!require(jsonlite)) {
  install.packages("jsonlite")
  library(jsonlite)
}

json_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.json"
chicago_bulls_list <- fromJSON(json_url)
chicago_bulls_list