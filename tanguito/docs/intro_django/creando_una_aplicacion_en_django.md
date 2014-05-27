#1.2. Creando una Aplicación en Django

Un proyecto en Django es una colección de configuraciones y aplicaciones que componen una aplicación web determinada o página web. Uno de los resultados esperados de la utilización de este enfoque es el de promover las buenas prácticas de ingeniería de software.

Existe una aplicación Django para realizar una tarea en particular. Es necesario crear aplicaciones específicas que son responsables de proporcionar al proyecto con cierto tipo particular de funcionalidades. Por ejemplo, podríamos imaginar que un proyecto puede consistir en varias aplicaciones, incluyendo una aplicación de votación, una aplicación de registro, y una aplicación relacionada con contenido específico. En otro proyecto, es posible que desee volver a utilizar la aplicación de votación y la aplicaciones de registro y utilizarlos para enviar, mostrar, publicar contenido diferente. Hay muchas aplicaciones Django que puede descargar y utilizar en sus proyectos. Vamos a creando nuestra propia aplicación.

Para empezar , cree una nueva aplicación llamada `rango`. Desde dentro de su directorio de proyecto Django (por ejemplo `<workspace>/tanguito`), ejecute el comando siguiente:

`(venv)$ python manage.py startapp rango`

El comando `startapp` crea un nuevo directorio en la raíz del proyecto. Como era de esperar, este directorio se llama `rango` - y contiene en su interior otros cuatro scripts de Python:

* `__init__.py`, sirviendo el mismo propósito exacto como se indicó anteriormente;
*`models.py`, un lugar para almacenar los modelos de datos de la aplicación - donde se especifica las entidades y relaciones entre los datos,
* `tests.py`, donde usted puede almacenar una serie de funciones para probar el código de su aplicación, es de los más importantes,
* `views.py`, donde usted puede almacenar una serie de funciones que toman las solicitudes del cliente y devuelven respuestas.

`views.py` y `models.py` son los dos archivos que va a utilizar para cualquier aplicación dada, y forman parte de los principales patrones de diseño arquitectónico empleado por Django, es decir, el patrón `Model-View-Template`. Usted puede comprobar la [documentación oficial de Django](https://docs.djangoproject.com/en/1.6/intro/overview/) para ver como modelos, vistas y plantillas se relacionan entre sí en más detalle.

Antes de poder empezar con la creación de sus propios modelos y vistas, debe configurar en su proyecto Django acerca de la existencia de su nueva aplicación. Para ello, es necesario modificar el archivo `settings.py`, contenido dentro del directorio de configuración de su proyecto `tanguito`. Abra el archivo y busque la tupla `INSTALLED_APPS`. Agregue la aplicación `rango` hasta el final de la tupla, que luego debe ser similar al siguiente ejemplo:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
)
```
Verifique que Django "registro" su nueva aplicación ejecutando el servidor de desarrollo de nuevo. Si puede iniciar el servidor sin errores, su aplicación fue configuradad y usted estará listo para continuar con el siguiente paso.
