# Django Vue Test

Proyecto usando Vue y Django para mostrar en Vue una lista de Notes recibidas de la
API de Django y un formulario para poder añadir Notes a nuestra lista. 

## Backend

``` bash
# opcionalmente, arrancar entorno virtual
## macOS y Linux:
python3 -m venv env
source env/bin/activate

## Windows:
py -m venv env
source env/Scripts/activate
```

En adelante, usaré python3 asumiento que el usuario esta en macOS o Linux.

```bash
# instalar dependencias
pip3 install -r requirements.txt

# Aplicar migrations
python3 manage.py migrate
```

Este punto es conveniente ya que en la app hacemos una query de usuarios, con este comando ya al menos tenemos uno

```bash
# Creacion de usuario admin
python3 manage.py createsuperuser

# Arrancar servidor en 127.0.0.1:8000
python3 manage.py runserver
```


## Frontend

``` bash
# navegar a la carpeta frontend
cd frontend

# instalar dependencias
npm install

# Arrancar app en localhost:8080
npm run dev
```

Una vez que esté todo arrancado correctamente, tan solo se ha de acceder a 
localhost:8080 y probar la app.