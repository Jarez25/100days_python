from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

print(datetime.hour)

now = datetime.now()

now = now.sleep()

print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.year)
print(now.month)

timestap = now.timestamp()

print(now.hour)
print (timestap)

year_2023 = datetime(2026, 1, 1, 3)

print(year_2023)

tiempo = time(21, 6, 3)

print(tiempo.hour)
print(tiempo.minute)
print(tiempo.second)

fecha = date(2023, 2, 25)

print(fecha.year)
print(fecha.month)
print(fecha.day)


fecha = date(fecha.year, fecha.month, fecha.day + 1)
print(fecha.day)

diff = year_2023 - now
print(diff)


tiempo_delta = timedelta(200, 100,1000, weeks= 10)
tiempo_delta_v2 = timedelta(300, 100, 100, weeks= 13)
print(tiempo_delta + tiempo_delta_v2)
print(tiempo_delta - tiempo_delta_v2)
print(tiempo_delta / tiempo_delta_v2)
###.... el timedelta nos e puede multiplicar
###......print(tiempo_delta * tiempo_delta_v2)