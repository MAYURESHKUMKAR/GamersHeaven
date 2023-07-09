# Generated by Django 4.2.1 on 2023-07-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0019_app_app_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppsGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='app',
            name='app_genre',
        ),
        migrations.AddField(
            model_name='app',
            name='app_genre',
            field=models.ManyToManyField(to='gheaven.genre'),
        ),
    ]
