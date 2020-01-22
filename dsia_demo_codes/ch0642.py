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

# 新增是否獲得總冠軍
is_champion = True
cb_list.append(is_champion)
cb_dict["is_champion"] = is_champion
print(cb_list[-1])            # 確認新增成功
print(cb_dict["is_champion"]) # 確認新增成功