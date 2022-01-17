# arquivo criado manualmente, pois, foi acrescentado às rotas
from django.urls import path
from . import views

# o django segue o padrao MVT, onde o models é a parte de DB, o V a logica python e o T o template,parte visual.
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logar/', views.logar, name="logar"),
    path('sair/', views.sair, name="sair")
]