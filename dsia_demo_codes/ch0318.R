if (!require("devtools")){
  install.packages("devtools")
}
if (!require("jsonlite")){
  install.packages("jsonlite")
} 
devtools::install_github("Kohze/fireData")
library(fireData)
library(jsonlite)

json_url <- "https://storage.googleapis.com/ds_data_import/boston_celtics_2007_2008.json"
boston_celtics_list <- fromJSON(json_url)

projectURL <- "YOURPROJECTURL" # 替換成自己的 Firebase 網址
upload(boston_celtics_list, projectURL = projectURL, directory = "boston_celtics")