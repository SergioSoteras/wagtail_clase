import json, requests
from lxml import html
#Sacar 200, la url paginada en 50 en 50

total = []

for i in range(1, 5):

    url = "https://www.livefutbol.com/maximos_goleadores_historicos/wm/tore/"+str(i)
    r = requests.get(url)
    pagina = html.fromstring(r.text)
    tabla = pagina.xpath("//table")[2]
    filas = tabla.xpath(".//tr")

    def datos_goleadores(goleador):
        '''Funcion que dado un elemento tr de una web devuelve los td de los datos del jugador
        '''

        datos={}

        elementos = goleador.xpath(".//td")
        #rank (Meterlo a mano al crear objeto, en la url algunos no tienen y da error).
        nombre = elementos[1]
        equipo = elementos[2]
        partidos = elementos[3]
        goles = elementos[4]
        penaltis = elementos[5]
        media = elementos[6]

        

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
        partidos_= partidos.xpath(".//text()")[0]
        datos['partidos']= partidos_

        #goles
        goles_ = goles.xpath(".//text()")[0]
        datos['goles'] = goles_

        #penaltis
        penaltis_ = penaltis.xpath(".//text()")[0]
        datos['penaltis'] = penaltis_

        #media
        media_ = media.xpath(".//text()")[0]
        datos['media'] = media_
        return datos

    datos = [datos_goleadores(goleador) for goleador in filas[1:51]]
    total.extend(datos)

    
json.dump(total, open("datos_goleadores.json", "w"))