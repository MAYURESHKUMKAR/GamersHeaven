# Generated by Django 4.2.1 on 2023-07-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0023_alter_activity_end_time_alter_activity_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
    ]
