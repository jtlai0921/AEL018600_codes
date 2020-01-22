team_name <- "Chicago Bulls"
season <- "1995-96"
records <- list(wins = 72, losses = 10)
coach <- "Phil Jackson"
assistant_coach <- c("Jim Cleamons", "John Paxson", "Jimmy Rodgers", "Tex Winter")
starting_lineups <- list(
  PG = "Ron Harper",
  SG = "Michael Jordan",
  SF = "Scottie Pippen",
  PF = "Dennis Rodman",
  C = "Luc Longley" 
)

# 以 list 儲存
cb_list <- list(team_name, season, records, coach, assistant_coach, starting_lineups)
# 以 named list 儲存
cb_named_list <- list(
  team_name = team_name,
  season = season,
  records = records,
  coach = coach,
  assistant_coach = assistant_coach,
  starting_lineups = starting_lineups
)

# 更新戰績
new_records <- list(
  wins = 72,
  losses = 10,
  winning_percent = sprintf("%.2f%%", 72/82*100)
)
cb_list[[3]] <- new_records
cb_named_list[["records"]] <- new_records
cb_list[[3]]               # 確定更新成功
cb_named_list[["records"]] # 確定更新成功