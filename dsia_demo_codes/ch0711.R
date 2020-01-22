numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers, player = players, stringsAsFactors = FALSE)
df[c(2, 3, 4), ]                                                                 # 透過位置
is_trio <- df$number %in% c(23, 33, 91)                                          # 透過球衣背號
is_trio
df[is_trio, ]
is_trio <- df$player %in% c("Michael Jordan", "Scottie Pippen", "Dennis Rodman") # 透過球員姓名
is_trio
df[is_trio, ]