# Generated by Django 4.1 on 2022-10-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacios',
            name='fechaEsp',
            field=models.DateTimeField(default=0, max_length=30),
        ),
    ]
