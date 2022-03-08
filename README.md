# wagtail_clase
Para el entorni virtual :
windows: python -m venv env
         pip install -r requirements.txt
         env\Scripts\activate.bat

linux:  python3 -m venv env
        pip install -r requirements.txt
        source env/bin/activate
        
# importar goleadores:
py manage.py shell
cd datos
%run extraer_goleadores.py
%run crear_goleadores.py

