numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
weights <- c(185, 195, 210, 210, 265)
df <- data.frame(number = numbers,
                 player = players,
                 weight = weights,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
df$weight_cat <- cut(df$weight, breaks = c(-Inf, 200, 250, Inf), labels = c("Light", "Medium", "Heavy"))
View(df)