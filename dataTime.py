import datetime

# b_date = datetime.date(1998,7,7)
# print(b_date)
# today = datetime.date.today()
# print(today)
# print(b_date.strftime('%A, %B, %d, %Y'))
#
# print(today-b_date)
# print(today.isoweekday())

# t = datetime.time(9,30,25,200000)
# print(t.hour)

t = datetime.datetime.today()
print(t)

t_delta = datetime.timedelta(days=20)
print(t-t_delta)
print(t+t_delta)