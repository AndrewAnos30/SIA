# Generated by Django 4.2 on 2023-05-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_alter_menudrinks_quantityao1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudrinks',
            name='hotAndCold',
            field=models.CharField(choices=[('hot', 'Hot'), ('cold', 'Cold'), ('both', 'Hot and Cold')], default='hot', max_length=4),
        ),
    ]