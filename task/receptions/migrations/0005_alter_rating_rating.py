# Generated by Django 4.0.2 on 2022-06-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptions', '0004_remove_reception_rating_remove_reception_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150),
        ),
    ]
