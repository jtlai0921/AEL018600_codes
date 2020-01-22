team_name = "Chicago Bulls"
season = "1995-96"
records = {
    "wins": 72,
    "losses": 10
}
coach = "Phil Jackson"
assistant_coach = ["Jim Cleamons", "John Paxson", "Jimmy Rodgers", "Tex Winter"]
starting_lineups = {
    "PG": "Ron Harper",
    "SG": "Michael Jordan",
    "SF": "Scottie Pippen",
    "PF": "Dennis Rodman",
    "C": "Luc Longley"
}

# 以 list 儲存
cb_list = [team_name, season, records, coach, assistant_coach, starting_lineups]
# 以 dict 儲存
cb_dict = {
    "team_name": team_name,
    "season": season,
    "records": records,
    "coach": coach,
    "assistant_coach": assistant_coach,
    "starting_lineups": starting_lineups
}
print(type(cb_list))
print(type(cb_dict))