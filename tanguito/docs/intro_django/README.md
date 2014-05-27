#1. Introducción a Django

```sh
$ virtualenv venv
New python executable in venv/bin/python
Installing Setuptools..............................................................................................................................................................................................................................done.
Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.
```
Activación del entorno de desarrollo
```sh
source venv/bin/activate
(venv)➜  tanguito git:(master) ✗
```
Instalación de Django
```sh
 (venv)$ pip install django
 ```

Instalando libreria de imagenes:

```sh
(venv)$ pip install PIL
```


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
