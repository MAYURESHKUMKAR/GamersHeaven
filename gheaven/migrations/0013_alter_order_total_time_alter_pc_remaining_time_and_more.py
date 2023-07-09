# Generated by Django 4.2.1 on 2023-07-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0012_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_time',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='pc',
            name='remaining_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='remaining_time',
            field=models.DurationField(),
        ),
    ]