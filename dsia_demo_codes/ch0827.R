numbers <- c(9, 23, 33, 91, 13, 7)
players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley", "Tony Kukoc")
colleges <- c("Miami University", "University of North Carolina", "University of Central Arkansas", "Southeastern Oklahoma State University", "University of New Mexico", NA)
df <- data.frame(number = numbers,
                 player = players,
                 college = colleges,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
!(is.na(df$college))
View(df[!(is.na(df$college)), ])