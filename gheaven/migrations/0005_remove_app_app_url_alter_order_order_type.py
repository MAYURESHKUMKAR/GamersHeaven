# Generated by Django 4.2.1 on 2023-07-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gheaven', '0004_alter_app_app_icon_url_alter_app_app_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='app_url',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('package', 'Package'), ('price', 'Price')], max_length=20),
        ),
    ]