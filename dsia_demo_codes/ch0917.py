from datetime import datetime, timedelta

first_day_of_2019 = datetime.strptime('2019-01-01', '%Y-%m-%d')
second_day_of_2019 = first_day_of_2019 + timedelta(days = 1)
last_day_of_2018 = first_day_of_2019 - timedelta(days = 1)
print(first_day_of_2019)
print(second_day_of_2019)
print(last_day_of_2018)
print(first_day_of_2019.strftime('%d, %B, %Y %H:%M:%S'))