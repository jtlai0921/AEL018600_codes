# 計算勝率或者從先發陣容中選出最喜歡的球員
winning_rate <- chicago_bulls_list$records$wins / (chicago_bulls_list$records$wins + chicago_bulls_list$records$losses)
fav_player <- chicago_bulls_list$starting_lineups$SG
sprintf("勝率為 %.2f", winning_rate)
sprintf("最喜歡的球員是 %s", fav_player)