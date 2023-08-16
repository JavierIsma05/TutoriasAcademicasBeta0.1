# Generated by Django 3.2 on 2023-08-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230816_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoria',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('accepted', 'Aceptada'), ('rejected', 'Rechazada')], default='pending', max_length=10),
        ),
    ]
