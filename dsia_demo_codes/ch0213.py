# 計算勝率或者從先發陣容中選出最喜歡的球員
winning_percentage = chicago_bulls_dict["records"]["wins"] / (chicago_bulls_dict["records"]["wins"] + chicago_bulls_dict["records"]["losses"])
fav_player = chicago_bulls_dict["starting_lineups"]["SG"]
print("勝率為 {:.2f}".format(winning_percentage))
print("最喜歡的球員是 {}".format(fav_player))