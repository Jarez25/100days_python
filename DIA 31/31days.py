import datetime
import locale #establece el idioma en espa;ol

hora = datetime.time(14,30,20,7777)
locale.setlocale(locale.LC_ALL, "es")


print(hora)
print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)

fecha = datetime.date(2027,12,20)

print(fecha)
print(fecha.year)
print(fecha.month)
print(fecha.day)

hoy = fecha.today()

print(hoy)

fecha_actual = datetime.datetime.now()

print(fecha_actual)

fecha_ahora = datetime.datetime.now()

fecha_con_formato = fecha_ahora.strftime('%A, %d de %B de %Y a las %H:%M')

print(fecha_con_formato)