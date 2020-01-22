fav_players <- c("Steve Nash", "Michael Jordan", "Paul Pierce", "Kevin Garnett", "Shaquille O'Neal")
fav_players                                                    # 移除母音前
gsub(fav_players, pattern = "[aeiouAEIOU]+", replacement = "") # 移除母音後