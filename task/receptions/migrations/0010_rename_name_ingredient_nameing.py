# Generated by Django 4.0.2 on 2022-06-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptions', '0009_ingredient_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='name',
            new_name='nameing',
        ),
    ]
