# Generated by Django 4.0.2 on 2022-06-01 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receptions', '0005_alter_rating_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('first_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
