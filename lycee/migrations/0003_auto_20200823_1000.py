# Generated by Django 3.0.8 on 2020-08-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0002_presence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateField(verbose_name='date of missing'),
        ),
    ]