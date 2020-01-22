csv_url <- "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df <- read.csv(csv_url, stringsAsFactors = FALSE)
head(df)           # 查看前六列觀測值
tail(df)           # 查看末六列觀測值
str(df)            # 查看資料框的複合資訊
summary(df)        # 查看描述性統計
dim(df)            # 查看資料框的外觀
nrow(df)           # 查看資料框有幾個列
ncol(df)           # 查看資料框有幾個欄
colnames(df)       # 查看資料框所有的變數名稱
row.names(df)[1:6] # 查看資料框的列索引值