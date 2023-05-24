# Generated by Django 4.2.1 on 2023-05-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='produtos.fornecedor'),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='produtos.marca'),
        ),
    ]
