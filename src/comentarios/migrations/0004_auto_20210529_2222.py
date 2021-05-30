# Generated by Django 3.1.7 on 2021-05-30 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_auto_20210529_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariofilme',
            name='comentario_pai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.comentariofilme'),
        ),
        migrations.AddField(
            model_name='comentariolivro',
            name='comentario_pai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.comentariolivro'),
        ),
        migrations.AddField(
            model_name='comentarioserie',
            name='comentario_pai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.comentarioserie'),
        ),
    ]
