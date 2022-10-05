# Generated by Django 4.1.1 on 2022-10-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0003_equipos'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacios',
            name='imageEsp',
            field=models.ImageField(default='', upload_to='png'),
        ),
        migrations.AddField(
            model_name='espacios',
            name='tipoEsp',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='espacios',
            name='caracteristicas',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='espacios',
            name='fechaEsp',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
