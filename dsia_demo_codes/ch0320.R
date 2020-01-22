if (!require("devtools")){
  install.packages("devtools")
}
devtools::install_github("Kohze/fireData")
library(fireData)

projectURL <- "YOURPROJECTURL" # 替換成自己的 Firebase 網址
fileName <- "boston_celtics/-LDj0KQInS4DDKvCxdDs" # 替換成自己的文件 id
boston_celtics_list <- download(projectURL = projectURL, fileName = fileName)
boston_celtics_list