# Generated by Django 5.1.4 on 2024-12-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbeto', '0002_rename_familiares_familiare_rename_niños_niño'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regalos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('regalo', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Familiare',
            new_name='Familiares',
        ),
        migrations.DeleteModel(
            name='Niño',
        ),
    ]
