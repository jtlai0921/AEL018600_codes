library(dplyr)

players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
numbers <- c(9, 23, 33, 91, 13)
colleges <- c("Miami University", "University of North Carolina", "University of Central Arkansas", "Southeastern Oklahoma State University", "University of New Mexico")
number_df <- data.frame(player = players,
                 number = numbers,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
college_df <- data.frame(player = players,
                         college = colleges,
                         stringsAsFactors = FALSE) # 避免處理 factor 型別
number_df %>% 
  inner_join(college_df) %>% 
  View()