import json, requests
from lxml import html
# datos = [datos_peli(peli) for peli in filas]
# json.dump(datos, open("datos_pelis.json", "w"))
url = "https://www.imdb.com/chart/top/"
r = requests.get(url)
pagina = html.fromstring(r.text)
tabla = pagina.xpath("//table")[0]
filas = tabla.xpath("//tbody/tr")

def datos_peli(peli):
    '''Funcion que dado un elemento tr de imdb con los datos de
       una pelicula devuelve un diccionario con los datos
    '''

    datos={}

    elementos = peli.xpath(".//td")
    imagen = elementos[0]
    titulo = elementos[1]
    rating_ = elementos[2]

    #imagen
    imagensrc = imagen.xpath(".//img/@src")[0]
    datos['img']=imagensrc

    #url de la peli
    url= titulo.xpath(".//a/@href")[0]
    datos['url']= url

    #cast
    cast =titulo.xpath(".//a/@title")[0]
    datos['cast'] = cast

    #titulo
    titulo_= titulo.xpath(".//a/text()")[0]
    datos['titulo']= titulo_

    #año
    year = titulo.xpath("./span/text()")[0].replace("(", "").replace(")", "")
    datos['year'] = year

    #rating
    rating = rating_.xpath(".//strong/text()")[0]
    datos['rating'] = rating

    #posicion
    place = imagen.xpath(".//span[@name='rk']/@data-value")[0]
    datos['place'] = place
    return datos

datos = [datos_peli(peli) for peli in filas]
json.dump(datos, open("datos_pelis.json", "w"))