# Generated by Django 5.1.4 on 2024-12-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbeto', '0006_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='apellido',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='regalo',
            name='apellido',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
