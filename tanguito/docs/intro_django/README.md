# Intro Django
## Test del Setup
Vamos a empezar por la comprobación de la instalaciones de Python, junto con Django, si, se han instalado correctamente, y se encuentran en la versión correcta para este tutorial:

> Para Python:

```bash
(venv)$ python --version
2.7.5
```
> Para Django:

```bash
(venv)$ python -c "import django; print(django.get_version())"
1.6.5
```

## Creando un Proyecto Django
Para crear un nuevo proyecto de Django, vaya a su directorio de código (es decir, el directorio `<workspace>`), y ejecute el comando siguiente:

`(venv)$ python django-admin.py startproject tanguito`

Este comando invoca el script `django-admin.py`, que pondrá en marcha un nuevo proyecto llamado Django `tanguito`.
Ahora se dará cuenta dentro de su área de trabajo `<workspace>` es un directorio que se establece en el nombre del nuevo proyecto, `tanguito`.
Dentro de este directorio recién creado, verá que hay dos elementos:

Un directorio con el mismo nombre que el proyecto, `tanguito`; y un script de Python llamada `manage.py`. Dentro del directorio del proyecto encontramos los siguientes documentos:

__init__.py, un script Python blanco cuya presencia indica al intérprete de Python que el directorio es un paquete de Python;
* `settings.py`, script `Python` donde se esta toda la configuración del proyecto construido con Django;
* `urls.py`, Almacena patrones de URL del proyecto; y
* `wsgi.py`, Se usa para ayudar a administrar el servidor de desarrollo e implementar el proyecto en un entorno de producción.

En el directorio del proyecto, usted verá que hay un archivo llamado `manage.py`. Estaremos llamando a este script a medida que desarrollamos nuestro proyecto, ya que le proporciona una serie de comandos que se pueden ejecutar para mantener su proyecto Django. Por ejemplo, `manage.py` le permite ejecutar el servidor de desarrollo integrado de Django para poner a prueba su código y ejecutar comandos para interactuar con la base de datos. Este script se utiliza mucho a lo largo del ciclo de desarrollo.

Ahora vamos a utilizar el script `manage.py` para tener el primer acercamiento de que nuestro proyecto funciona:

`$ python manage.py runserver`

Al ejecutar este comando le indicará a Django iniciar el servidor de desarrollo de peso ligero. Usted debe ver a la salida en su terminal similar al ejemplo que se muestra a continuación:

```sh
$ python manage.py runserver

Validating models...

0 errors found
September 21, 2013 - 06:12:41
Django version 1.5.4, using settings 'tango_with_django_project.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Puede detener el servidor de desarrollo en cualquier momento presionando `CTRL + C` en la ventana de terminal.

Para utilizar un puerto diferente al que viene definido por defecto en Django, lo puede hacer de siguiente manera:

`$ python manage.py runserver <your_ip_address>:5555`

