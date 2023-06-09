# Generated by Django 4.2.1 on 2023-05-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=255)),
                ('referencia_fornecedor', models.TextField(max_length=255)),
                ('preco_custo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=4)),
                ('data_compra', models.DateField()),
                ('ultima_modificacao', models.DateField(auto_now=True)),
                ('ncm', models.CharField(max_length=8)),
            ],
        ),
    ]
