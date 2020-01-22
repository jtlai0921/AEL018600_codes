# JSON 檔案儲存在本機
from json import load

json_fp = "chicago_bulls_1995_1996.json"
with open(json_fp) as f:
    chicago_bulls_dict = load(f)
print(type(chicago_bulls_dict))
chicago_bulls_dict