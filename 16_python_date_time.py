from datetime import date,datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f'{day},{month},{year},{hour},{minute},{timestamp}')
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_one)
today = '5 December, 2019'
date_object = datetime.strptime(today, '%d %B, %Y')
print(date_object)
new_year = date(year=2027, month=1, day=1)
now_year = date(year=year,month=month,day=day)
time_left_for_newyear = new_year - now_year
print('The left time for new year: ',time_left_for_newyear)
mukaasi = date(year=1970,month=1,day=1)
difference_mukasi = now_year - mukaasi
print('The passed time from 1970: ',difference_mukasi)
