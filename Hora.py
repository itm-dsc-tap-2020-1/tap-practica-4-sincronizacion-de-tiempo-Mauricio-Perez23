import datetime
import ntplib
import os
from time import ctime

servidor= "ntp2.recro.ae"
cliente = ntplib.NTPClient()
t1 = datetime.datetime.now()
print("--> Hora de petición (t1): "+str(t1))


respuesta = cliente.request(servidor)
t2 = datetime.datetime.now()
print("--> Hora de recepción (t2): "+str(t2))


hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("--> Hora del servidor: "+str(hora_actual))
ajuste = (t2-t1)/2
print("--> Ajuste: "+str(ajuste))

Rel=hora_actual + ajuste
print("---> Actualización: "+str(Rel)+"\n")
os.system(f"date --set '{Rel}'")
print("\n")