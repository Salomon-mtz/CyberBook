# Generated by Django 4.1.1 on 2022-10-09 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cyber', '0010_alter_equipos_id_alter_espacios_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
