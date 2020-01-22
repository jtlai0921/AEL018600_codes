import re

def remove_vowels(x):
  ans = re.sub(pattern="[aeiouAEIOU]+", repl="", string=x)
  return ans

fav_players = ["Steve Nash", "Michael Jordan", "Paul Pierce", "Kevin Garnett", "Shaquille O'Neal"]
print(fav_players)                           # 移除母音前
print(list(map(remove_vowels, fav_players))) # 移除母音後