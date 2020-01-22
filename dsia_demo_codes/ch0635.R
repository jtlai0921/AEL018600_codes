numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers, player = players, stringsAsFactors = FALSE)
df[2, 2] # # Michael Jordan 位於 (2, 2)