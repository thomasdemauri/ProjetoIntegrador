from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=80)
    nome_fantasia = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero_logradouro = models.CharField(max_length=5)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.razao_social


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    referencia_fornecedor = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default="")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, default="")
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()
    ultima_modificacao = models.DateField(auto_now=True) # Adiciona a data no momento da execucao do comando save()
    ncm = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.descricao + " | " + self.referencia_fornecedor


    def formata_data_compra(self):
        return self.data_compra.strftime('%Y-%m-%d')


    def formata_ultima_modificacao(self):
        return self.ultima_modificacao.strftime('%Y-%m-%d')