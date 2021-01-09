# Generated by Django 3.0.11 on 2021-01-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210109_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='serving_size',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit_of_measurement',
            field=models.CharField(choices=[('OZ', 'Ounces'), ('LBS', 'Pounds'), ('GR', 'Grams'), ('FLOZ', 'Fluid Ounces'), ('CUPS', 'Cups')], default='GR', max_length=4),
        ),
    ]