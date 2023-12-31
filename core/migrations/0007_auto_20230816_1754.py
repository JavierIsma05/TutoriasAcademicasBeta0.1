# Generated by Django 3.2 on 2023-08-16 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_tutoria_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoria',
            name='firma',
            field=models.ImageField(default='default.png', upload_to='firmas/', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='tutoria',
            name='modalidad',
            field=models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual')], default='P', max_length=10, verbose_name='Modalidad'),
        ),
    ]
