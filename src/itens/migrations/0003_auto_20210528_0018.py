# Generated by Django 3.1.7 on 2021-05-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_auto_20210527_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='tipo_item',
            field=models.CharField(default='filme', max_length=100, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='livro',
            name='tipo_item',
            field=models.CharField(default='filme', max_length=100, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='serie',
            name='tipo_item',
            field=models.CharField(default='filme', max_length=100, verbose_name='Tipo'),
        ),
    ]