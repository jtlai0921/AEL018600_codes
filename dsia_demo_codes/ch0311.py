from pandas_gbq import read_gbq

project_id = 'YOURPROJECTID'
private_key = 'YOURSERVICEACCOUNT'
sql_statement = "SELECT * FROM fav_nba_teams.chicago_bulls;"
chicago_bulls = read_gbq(sql_statement, project_id=project_id, private_key=private_key)
chicago_bulls