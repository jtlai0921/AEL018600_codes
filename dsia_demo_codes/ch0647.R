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
# 迭代 list
for (i in 1:length(cb_list)) {
  print(sprintf("位於索引值 %i 的元素是：", i))
  print(cb_list[[i]])
}
print("============")
# 迭代 named list
cb_list_names <- names(cb_named_list)
for (i in 1:length(cb_list_names)) {
  print(sprintf("位於標籤 %s 的元素是：", cb_list_names[i]))
  print(cb_named_list[[cb_list_names[i]]])
}