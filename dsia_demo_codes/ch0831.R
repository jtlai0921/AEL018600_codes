numbers <- c(9, 23, 33, 91, 13)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
birth_dates <- c("January 20, 1964", "February 17, 1963", "September 25, 1965", "May 13, 1961", "January 19, 1969")
df <- data.frame(number = numbers,
                 player = players,
                 birth_date = birth_dates,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
df$birth_date <- as.Date(df$birth_date, format = "%B %d, %Y")
class(df$birth_date)
View(df)