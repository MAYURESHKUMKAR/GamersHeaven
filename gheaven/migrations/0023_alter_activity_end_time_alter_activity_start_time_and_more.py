# Generated by Django 4.2.1 on 2023-07-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0022_alter_order_package_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_and_time',
            field=models.DateField(auto_now=True),
        ),
    ]
