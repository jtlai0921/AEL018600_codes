numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers,
                 player = players,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
class(df$number)
df$number
df$number <- as.character(df$number)
class(df$number)
df$number