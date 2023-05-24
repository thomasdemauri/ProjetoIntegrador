from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from . models import Produto, Fornecedor, Marca

# -->   Aqui ficam todas as funcoes responsaveis por tratar os dados capturados do
#       banco de dados e envia-las para um template html <--

# Essa requisicao trata de apenas renderizar a pagina inicial
def index(requisicao):
    #return HttpResponse("Olaaaa")
    return render(requisicao, "produtos/index.html")


# Essa requisicao trata de capturar do banco de dados todos os produtos e 
# retornar isso para o template atraves do dicionario 'contexto'
def todos_produtos(requisicao):
    try:
        todos_produtos =  Produto.objects.all()
        contexto = { "todos_produtos" : todos_produtos }
    except Produto.DoesNotExist:
        raise Http404("Erro ")
    return render(requisicao, "produtos/todos_produtos.html", contexto)

# Essa requisicao trata de capturar do banco de dados o ID igual a chave primaria (id) de produto e 
# se existir um, é retornado tal produto para o template atraves do dicionario 'contexto'
def produto_detalhado(requisicao, id_produto):
    try:
        produto = Produto.objects.get(pk=id_produto)
        contexto = { "produto" : produto }
        print(produto.data_compra)
    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    return render(requisicao, "produtos/produto_detalhado.html", contexto)


def editar_produto(requisicao, id_produto):
    try:
        produto = Produto.objects.get(pk=id_produto)

        produto.descricao = requisicao.POST["descricao"]
        produto.referencia_fornecedor = requisicao.POST["referencia_fornecedor"]
        # Nao da pra fazer o mesmo com marca, uma vez que a mesma e chave estrangeira
        # Pensar depois em como alterar
        # Nao da pra fazer o mesmo com fornecedor, uma vez que o mesmo e chave estrangeira
        # Pensar depois em como alterar
        produto.preco_custo = requisicao.POST["preco_custo"]
        produto.preco_venda = requisicao.POST["preco_venda"]
        produto.data_compra = requisicao.POST["data_compra"]
        produto.ncm = requisicao.POST["ncm"]

        produto.save()
    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    return HttpResponseRedirect(reverse("produtos:todos_produtos"))

    



#################### Fornecedor ################

# Essa requisicao trata de capturar do banco de dados todos os fornecedores e 
# retornar isso para o template atraves do dicionario 'contexto'
def todos_fornecedores(requisicao):
    try:
        todos_fornecedores = Fornecedor.objects.all()
        contexto = { "todos_fornecedores" : todos_fornecedores }
    except Fornecedor.DoesNotExist:
        raise Http404("Erro ao tentar exibir todos os fornecedores!")
    return render(requisicao, "produtos/todos_fornecedores.html", contexto)
    