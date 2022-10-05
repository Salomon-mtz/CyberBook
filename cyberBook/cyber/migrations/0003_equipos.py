# Generated by Django 4.1 on 2022-10-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0002_alter_espacios_fechaesp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('idEq', models.CharField(default=0, max_length=50, primary_key=True, serialize=False)),
                ('fechaEq', models.CharField(default=0, max_length=30)),
                ('tipoEq', models.CharField(default=0, max_length=20)),
                ('caracteristicas', models.CharField(default=0, max_length=50)),
                ('tiempoEq', models.IntegerField()),
                ('disponibleEq', models.BooleanField()),
            ],
        ),
    ]