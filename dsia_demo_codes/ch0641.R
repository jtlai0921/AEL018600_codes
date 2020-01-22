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
cb_list[[5]][2]                             # 選出助理教練 John Paxson
cb_named_list[["starting_lineups"]][["SG"]] # 選出 Michael Jordan