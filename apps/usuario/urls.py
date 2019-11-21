from django.contrib import admin
from django.urls import path
from .views import PaginaInicio, Premios, Registro, signup, IniciarSesion, postsignup

urlpatterns = [
    # 1. url de la pagina (PaginaInicio/), 2. el nombre de la funcion, 3. Alias de la pagina
    path('', PaginaInicio, name='inicio'),
    path('premios.html/', Premios, name='premios'),
    path('registro.html/', Registro, name='registro'),
    path('signup/', signup, name='signup'),
    path('iniciarsesion.html', IniciarSesion, name='iniciarsesion'),
    path('postsignup/', postsignup, name='postsignup')
]
