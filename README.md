# Instrucciones para ejecutar este proyecto

- Crear Directorio del proyecto Library

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Crear directorio de trabajo para el proyecto de Librería 
```bash
cd
mkdir -p Documents/library
cd Documents/library
ls 
```

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/rgbe07/entrega1-bernal-esparza/

cd library

git checkout master
```

### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Navegamos hacia la carpeta del proyecto `library`
```bash
cd library
```

### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```

### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### 8. Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 

### 9. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

- Es hora de ir al navegador y en una pestaña nueva navegar hacia `http://127.0.0.1:8000/

Hay opciones para crear libro, sección y ebook
en el menú superior se puede listar cada uno de ellos cuando ya han sigo creados.
