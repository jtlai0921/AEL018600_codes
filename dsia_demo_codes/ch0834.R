library(tidyr)

players <- c("Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley")
heights <- c("6-6", "6-6", "6-8", "6-7", "7-2")
weights <- c(185, 195, 210, 210, 265)
df <- data.frame(player = players,
                 height = heights,
                 weight = weights,
                 stringsAsFactors = FALSE) # 避免處理 factor 型別
df %>% 
  gather(key = "key", value = "value", height, weight) %>% # 轉換為長表格
  View()