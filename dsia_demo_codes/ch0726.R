numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers, player = players, stringsAsFactors = FALSE)
df$team <- "Chicago Bulls"
df$height <- c("6-6", "6-6", "6-8", "6-7", "7-2")
View(df)