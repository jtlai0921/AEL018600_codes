get_position <- function(player) {
  if (player == "Ron Harper") {
    return("PG")
  } else if (player == "Michael Jordan") {
    return("SG")
  } else if (player == "Scottie Pippen") {
    return("SF")
  } else if (player == "Dennis Rodman") {
    return("PF")
  } else {
    return("C")
  }
}

numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers,
                 player = players,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
df$position <- sapply(df$player, FUN = get_position)
df$court <- ifelse(df$position %in% c("PG", "SG"), "Back", "Front")
View(df)