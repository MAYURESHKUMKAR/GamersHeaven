# Generated by Django 4.2.1 on 2023-07-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0014_alter_activity_end_time_alter_activity_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]