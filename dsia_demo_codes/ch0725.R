players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
df <- data.frame(number = numbers, player = players, stringsAsFactors = FALSE)
get_last_name <- function(x) {
  split_lst <- strsplit(x, split = " ")
  name_length <- length(split_lst[[1]])
  last_name <- split_lst[[1]][name_length]
  return(last_name)
}
df$last_name <- sapply(df$player, FUN = get_last_name)
View(df)