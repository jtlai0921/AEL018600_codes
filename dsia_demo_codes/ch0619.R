arr <- c(TRUE, FALSE, 87L)      # 同時有邏輯值與整數換為整數
arr
class(arr)
writeLines("\n")
arr <- c(arr, 8.7)              # 同時有邏輯值、整數與浮點數換為浮點數
arr
class(arr)
writeLines("\n")
arr <- c(arr, "Luke Skywalker") # 同時有邏輯值、整數、浮點數與文字換為文字
arr
class(arr)