# Generated by Django 4.1.1 on 2022-10-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0008_remove_equipos_ideq_remove_espacios_idesp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='espacios',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]