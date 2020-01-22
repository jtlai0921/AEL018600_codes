if (!require(RMySQL)) {
  install.packages("RMySQL")
  library(DBI)
}

host <- "YOURHOST" # 輸入自己的 AWS RDS Enpoint 位址
port <- 3306
dbname <- "YOURDBNAME" # 輸入自己設定的資料庫名稱
user <- "YOURUSERNAME" # 輸入自己設定的使用者名稱
password <- "YOURPASSWORD" # 輸入自己設定的使用者密碼

engine <- dbConnect(RMySQL::MySQL(),
                    host = host,
                    port = port,
                    dbname = dbname,
                    user = user,
                    password = password
                    )
boston_celtics <- dbReadTable(engine, name = 'boston_celtics')
View(boston_celtics)