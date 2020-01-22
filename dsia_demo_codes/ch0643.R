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
# 新增是否獲得總冠軍
is_champion <- TRUE
cb_list <- c(cb_list, is_champion)
cb_named_list[["is_champion"]] <- is_champion
cb_list[[length(cb_list)]]     # 確認新增成功
cb_named_list[["is_champion"]] # 確認新增成功