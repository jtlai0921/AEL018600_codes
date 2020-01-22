# JSON 檔案儲存在雲端
from requests import get

json_url = 'https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.json'
chicago_bulls_dict = get(json_url).json()
print(type(chicago_bulls_dict))
chicago_bulls_dict