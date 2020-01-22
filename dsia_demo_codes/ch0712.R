library(dplyr)

numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers, player = players, stringsAsFactors = FALSE)
df %>% 
  filter(number %in% c(23, 33, 91)) # filter(player %in% c("Michael Jordan", "Scottie Pippen", "Dennis Rodman"))