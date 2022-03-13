# wagtail_clase
Para la instalación del entorno virtual :     
- Windows:       
1. python -m venv env
2. pip install -r requirements.txt   
3. env\Scripts\activate.bat   
- Linux:      
1. python3 -m venv env
2. pip install -r requirements.txt
3. source env/bin/activate
        
# importar goleadores:
1. py manage.py shell
2. cd datos
3. %run extraer_goleadores.py
4. %run crear_goleadores.py
# importar peliculas:
1. py manage.py shell
2. cd datos
3. %run extraer_pelis.py
4. %run crear_peliculas.py
# Uso del Blog
Contiene tres aplicaciones el proyecto, blog, peliculas y goleadores.
- Blog    
Contiene la mayoria de páginas y modelos. Contiene la página con el formulario de contacto, las noticias y un BlogIndexPage que solo podrá ser hija de la página Home, y solo podrá tener 3 hijas:        
    1. BlogPage: Comunicar cualquier informacion, con sus tags y sus categorías.
    2. ViajesPage: Comunicar un viaje, con fotos y coordenadas, que mostrará en el template con un mapa.
    3. PeliCommentPage: Añadir comentarios a las películas que tenemos en la app Peliculas.
- Peliculas    
Contiene el modelo del index de Peliculas , que recogerá todos los objetos de Pelicula, creados como Snippet.
- Goleadores    
Contiene el modelo del index de Goleadores , que recogerá todos los objetos de Goleadores, creados como Snippet, y el genericView de cada Goleador.del blog
- Componentes base del blog:    
    1. Navbar con las diferentes secciones del blog para navegar fácilmente.
    2. Footer editable desde el admin, en los snippet editando el footer text.
    3. Sidebar que contiene la lista de las ultimas 5 noticias y todas las tags de los post para buscar los post relacinados con ellas rápidamente.  
