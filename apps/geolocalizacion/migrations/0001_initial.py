# Generated by Django 2.1 on 2019-01-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('latitudubicacion', models.CharField(blank=True, help_text='Ingrese la Latitud', max_length=30, null=True, verbose_name='Latitud')),
                ('longitudubicacion', models.CharField(blank=True, help_text='Ingrese la Longitud', max_length=30, null=True, verbose_name='Longitud')),
                ('descripcionubicacion', models.CharField(blank=True, help_text='Ingrese Descripcion de la Ubicacion', max_length=50, null=True, verbose_name='Descripcion de la Ubicacion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
