first_day_of_2019 <- as.Date('2019-01-01')
second_day_of_2019 <- first_day_of_2019 + 1
last_day_of_2018 <- first_day_of_2019 - 1
first_day_of_2019 <- as.POSIXct(first_day_of_2019)
format(first_day_of_2019, '%Y-%m-%d %H:%M:%S', tz = 'GMT')
format(second_day_of_2019, '%Y-%m-%d %H:%M:%S', tz = 'GMT')
format(last_day_of_2018, '%Y-%m-%d %H:%M:%S', tz = 'GMT')
format(first_day_of_2019, '%d, %B, %Y %H:%M:%S', tz = 'GMT')