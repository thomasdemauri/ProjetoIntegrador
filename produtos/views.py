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


# Essa requisicao apenas obtem forncedores e marcas do bd, renderiza o formulario
# Assim que o formulario e submetido envia para funcao que salva de fato o novo produto no bd
def incluir_produto(requisicao):
    try:
        fornecedores = Fornecedor.objects.all()
        marcas = Marca.objects.all()

        # A redundancia em atual_fornecedor e atual_marca e devida a hora de verificar e igual, so funciona comparando string com string
        contexto = { 
            "fornecedores" : fornecedores, 
            "marcas" : marcas,
        }
    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    except Marca.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    return render(requisicao, "produtos/incluir_produto.html", contexto)


# Essa funcao apenas obtem os dados do formulario e cria de fato um novo produto
# Redirecionando para todos_produtos
def salva_produto_bd(requisicao):
    descricao = requisicao.POST["descricao"]
    referencia_fornecedor = requisicao.POST["referencia_fornecedor"]
    marca = Marca.objects.get(nome=requisicao.POST["marca"])
    fornecedor = Fornecedor.objects.get(razao_social=requisicao.POST["fornecedor"])
    preco_custo = requisicao.POST["preco_custo"]
    preco_venda = requisicao.POST["preco_venda"]
    data_compra = requisicao.POST["data_compra"]
    ncm = requisicao.POST["ncm"]
    novo_produto = Produto.objects.create(descricao=descricao,
                                          referencia_fornecedor=referencia_fornecedor,
                                          marca=marca,
                                          fornecedor=fornecedor,
                                          preco_custo=preco_custo,
                                          preco_venda=preco_venda,
                                          data_compra=data_compra,
                                          ncm=ncm
                                        )
    novo_produto.save()
    return HttpResponseRedirect(reverse("produtos:todos_produtos"))



# Essa requisicao trata de capturar do banco de dados todos os produtos e 
# retornar isso para o template atraves do dicionario 'contexto'
def todos_produtos(requisicao):
    try:
        todos_produtos =  Produto.objects.order_by("-id").all()
        contexto = { "todos_produtos" : todos_produtos }
    except Produto.DoesNotExist:
        raise Http404("Erro ")
    return render(requisicao, "produtos/todos_produtos.html", contexto)


# Essa requisicao trata de capturar do banco de dados o ID igual a chave primaria (id) de produto e 
# se existir um, é retornado tal produto para o template atraves do dicionario 'contexto'
def produto_detalhado(requisicao, id_produto):
    try:
        produto = Produto.objects.get(pk=id_produto)
        fornecedores = Fornecedor.objects.all()
        marcas = Marca.objects.all()

        # A redundancia em atual_fornecedor e atual_marca e devida a hora de verificar e igual, so funciona comparando string com string
        contexto = { 
            "produto" : produto, 
            "fornecedores" : fornecedores, 
            "atual_fornecedor" : str(produto.fornecedor), 
            "marcas" : marcas,
            "atual_marca" : str(produto.marca),
        }

    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    return render(requisicao, "produtos/produto_detalhado.html", contexto)


# Essa requisicao trata de captura atraves do metodo POST os valores obtidos no formulario
# e atualizar o registro no banco de dados. Apos isso ele redireciona para o a view 'produto_detalhado'
def editar_produto(requisicao, id_produto):
    try:
        produto = Produto.objects.get(pk=id_produto)

        produto.descricao = requisicao.POST["descricao"]
        produto.referencia_fornecedor = requisicao.POST["referencia_fornecedor"]
        produto.marca = Marca.objects.get(nome=requisicao.POST["marca"])
        produto.fornecedor = Fornecedor.objects.get(razao_social=requisicao.POST["fornecedor"])
        produto.preco_custo = requisicao.POST["preco_custo"]
        produto.preco_venda = requisicao.POST["preco_venda"]
        produto.data_compra = requisicao.POST["data_compra"]
        produto.ncm = requisicao.POST["ncm"]

        produto.save()
    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar detalhar um produto")
    return HttpResponseRedirect(reverse("produtos:todos_produtos"))

    
# Essa requisicao exclui o produto e redireciona para o view todos_produtos
def excluir_produto(requisicao, id_produto):
    try:
        Produto.objects.get(pk=id_produto).delete()
    except Produto.DoesNotExist:
        raise Http404("Erro ao tentar excluir o produto")
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
    