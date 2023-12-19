# Generated by Django 5.0 on 2023-12-19 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Género del libro', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumen', models.TextField(help_text='Introduce un resumen del libro.', max_length=1000)),
                ('isbn', models.CharField(help_text='Introduce el ISBN', max_length=13, unique=True, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='miAplicacion.autor')),
                ('genero', models.ManyToManyField(help_text='Escoge el género', to='miAplicacion.genero')),
            ],
        ),
    ]