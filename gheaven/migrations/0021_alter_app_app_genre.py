# Generated by Django 4.2.1 on 2023-07-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0020_appsgenre_remove_app_app_genre_app_app_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_genre',
            field=models.ManyToManyField(to='gheaven.appsgenre'),
        ),
    ]