# Generated by Django 5.1.4 on 2024-12-09 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbeto', '0003_regalos_rename_familiare_familiares_delete_niño'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Familiares',
            new_name='Familiare',
        ),
        migrations.RenameModel(
            old_name='Regalos',
            new_name='Regalo',
        ),
    ]
