'''
crear goleadores
ejecutar:
python manage.py shell < datos/crear_peliculas.py
'''

from goleadores.models import Goleador
import json
import os


# borrar pelis
for g in Goleador.objects.all():
    g.delete()

#lista de películas del json
if os.path.exists("datos/datos_goleadores.json"):
    goleadores = json.load(open("datos/datos_goleadores.json"))
else:
    goleadores = json.load(open("datos_goleadores.json"))

rank=1

for goleador in goleadores:
    g = Goleador()
    g.rank = rank
    g.nombre = goleador["nombre"]
    g.icono= goleador["icono"]
    g.seleccion = goleador["seleccion"]
    g.partidos =  goleador["partidos"]
    g.goles =  goleador["goles"]
    g.penaltis =  goleador["penaltis"]
    g.media =  goleador["media"]
    g.save()
    rank +=1