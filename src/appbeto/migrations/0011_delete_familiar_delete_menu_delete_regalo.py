# Generated by Django 5.1.4 on 2024-12-30 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbeto', '0010_alter_misblog_icono'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Familiar',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Regalo',
        ),
    ]
