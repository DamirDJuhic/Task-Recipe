# Generated by Django 4.0.2 on 2022-05-28 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='reception_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
