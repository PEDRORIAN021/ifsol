# Generated by Django 4.2.6 on 2023-12-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_carrinho_itemcarrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrinho',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]