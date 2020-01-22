get_weight_cat <- function(weight) {
  if (weight < 200) {
    return("Light")
  } else if (weight >= 200 & weight < 250) {
    return("Medium")
  } else {
    return("Heavy")
  }
}

numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
weights <- c(185, 195, 210, 210, 265)
df <- data.frame(number = numbers,
                 player = players,
                 weight = weights,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
df$weight_cat <- sapply(df$weight, FUN = get_weight_cat)
View(df)