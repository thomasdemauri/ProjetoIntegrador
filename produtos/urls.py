from django.contrib import admin
from django.urls import path
from . import views

app_name = "produtos"
urlpatterns = [
    path('', views.index, name="index"),
    path('todos_produtos/', views.todos_produtos, name="todos_produtos"),
    path('produto_detalhado/<int:id_produto>/', views.produto_detalhado, name="produto_detalhado"),
    path('editar_produto/<int:id_produto>/', views.editar_produto, name="editar_produto"),
    path('excluir_produto/<int:id_produto>/', views.excluir_produto, name="excluir_produto"),
    path('incluir_produto/', views.incluir_produto, name="incluir_produto"),
    path('salva_produto_bd/', views.salva_produto_bd, name="salva_produto_bd"),

    
    # Fornecedores 
    path('todos_fornecedores/', views.todos_fornecedores, name="todos_fornecedores"),
]
