# Generated by Django 4.0.2 on 2022-03-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_post_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='blogApp.Categoria'),
        ),
    ]
