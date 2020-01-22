import re

shaq = "Shaquille O'Neal"
print(re.split(pattern="\s+", string=shaq))             # 以空格分隔
print(len(re.findall(pattern="\s+", string=shaq)) > 0)  # 判斷是否有空格
print(re.sub(pattern="\s+", repl=';', string=shaq))     # 將空格取代為分號