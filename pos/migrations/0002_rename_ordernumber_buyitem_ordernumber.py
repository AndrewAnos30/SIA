# Generated by Django 4.2.1 on 2023-05-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyitem',
            old_name='ordernumber',
            new_name='orderNumber',
        ),
    ]