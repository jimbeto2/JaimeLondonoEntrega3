# Generated by Django 5.1.4 on 2024-12-09 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbeto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Familiares',
            new_name='Familiare',
        ),
        migrations.RenameModel(
            old_name='Niños',
            new_name='Niño',
        ),
    ]
