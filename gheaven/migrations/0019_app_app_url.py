# Generated by Django 4.2.1 on 2023-07-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0018_alter_app_app_icon_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app_url',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
