import json, requests
from lxml import html

url = "https://www.livefutbol.com/maximos_goleadores_historicos/wm/tore/1/"
r = requests.get(url)
pagina = html.fromstring(r.text)
tabla = pagina.xpath("//table")[2]
filas = tabla.xpath(".//tr")
#goleador = filas[1].xpath(".//td")
def datos_goleadores(goleador):
    '''Funcion que dado un elemento tr de una web devuelve los td de los datos del jugador
    '''

    datos={}

    elementos = goleador.xpath(".//td")
    rank = elementos[0]
    nombre = elementos[1]
    equipo = elementos[2]
    partidos = elementos[3]
    goles = elementos[4]
    penaltis = elementos[5]
    media = elementos[6]

    #rank
    rank_ = rank.xpath("./text()")[0]
    datos['rank'] = rank_

    #nombre
    nombre_= nombre.xpath("./a/text()")[0]
    datos['nombre'] = nombre_

    #equipo
    #icono
    icono = equipo.xpath(".//img/@src")[0]
    datos['icono'] = icono
    #seleccion
    seleccion = equipo.xpath(".//a[2]/text()")[0]
    datos['seleccion'] = seleccion

    #partidos
    partidos_= partidos.xpath("./text()")[0]
    datos['partidos']= partidos_

    #goles
    goles_ = goles.xpath("./text()")[0]
    datos['goles'] = goles_

    #penaltis
    penaltis_ = penaltis.xpath("./text()")[0]
    datos['penaltis'] = penaltis_

    #media
    media_ = media.xpath("./text()")[0]
    datos['media'] = media_
    return datos

datos = [datos_goleadores(goleador) for goleador in filas[2:3]]
json.dump(datos, open("datos_goleadores.json", "w"))