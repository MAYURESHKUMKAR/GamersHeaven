# Generated by Django 4.2.1 on 2023-07-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0002_genre_rename_game_description_game_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='icon_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='video_url',
            field=models.TextField(),
        ),
    ]