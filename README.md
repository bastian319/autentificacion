## Configuracion del entorno
```bash
python  -m venv venv
```
## Activacion del entorno
```bash
venv\Scripts\Activate
```

## Configuracion inicial de dependencia de requeriments.txt
```bash
asgiref==3.12.1
cffi==2.1.1
cryptography==50.0.2
Django==5.0.14
mysqlclient==2.3.0
pycparser==3.11
PyMySQL==1.2.3
sqlparse==0.6.0
tzdata==2026.5
```

## Instalar django y guardar dependencias
```bash
pip install -r requeriments.txt
```

## Pasos del proyecto
```bash
django-admin startproject proyecto_autentificacion .
```

## Al crear el proyecto_autentificacion, iremos a la carpeta __init.py, agregamos el codigo para que salga la instalacion 
```bash
import pymysql
```

## Creamos la base de datos pero tambien se puede hacer de manera manual
```bash
create database bd_autentificacion;
```

## Cambiamos la base de datos con nuestro usuario y credenciales
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bd_autentificacion',
        'USER':'root',
        'PASSWORD':'',
    }
}
```

## De paso cambiamos el idioma
```bash
LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/santiago'

USE_I18N = True

USE_TZ = True
```

## Revisamos si estan correctos los templates
```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Hacemos las migraciones correspondientes
```bash
py manage.py migrate
```

## Creamos el super usuario
```bash
py manage.py createsuperuser
```

## Por motivos de aprendizaje y no seguridad esta vez seran las credenciales
```bash
admin
admin@gmail.com
admin1234
y
```

## Creamos la aplicacion
```bash
py manage.py startapp autentificacion_app
```

## Conectamos el proyecto con la aplicacion (autentificacion_app)
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autentificacion_app',
]
```

## Vamos a crear las vistas en autentificacion_app/views.py
```bash
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

## Creacion de vista

def index(request):
    return render (request, 'autentificacion_app/index.html')

def home(request):
    return render (request, 'autentificacion_app/home.html')

@login_required
def login(reuqest):
    return render (request, 'autentificacion_app/login.html')
```

## Necesito configurar la url en proyecto_autentificacion, voy a urls.py
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('autentificacion_app.urls')) 
]
```

## En autentificacion_app creo la urls.py
```bash
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(templates_name='autentificacion_app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
]
```

## Ingreso al proyecto autentificacion setting.py
```bash
STATIC_URL = 'static/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/home'
```