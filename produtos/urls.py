from django.contrib import admin
from django.urls import path
from . import views

app_name = "produtos"
urlpatterns = [
    path('', views.index, name="index"),
    path('todos_produtos/', views.todos_produtos, name="todos_produtos"),
    path('produto_detalhado/<int:id_produto>/', views.produto_detalhado, name="produto_detalhado"),
    path('editar_produto/<int:id_produto>/', views.editar_produto, name="editar_produto"),
    # Fornecedores 
    path('todos_fornecedores/', views.todos_fornecedores, name="todos_fornecedores"),
]
