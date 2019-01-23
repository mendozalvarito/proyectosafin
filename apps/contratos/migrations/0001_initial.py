# Generated by Django 2.1 on 2019-01-23 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooperativa', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('referenciacontrato', models.CharField(blank=True, help_text='Ingrese Referencia del Contrato', max_length=50, null=True, verbose_name='Referencia Contrato')),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('Direccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Direccion')),
                ('Planservicios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperativa.Planservicios')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
