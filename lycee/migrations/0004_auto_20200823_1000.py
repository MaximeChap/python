# Generated by Django 3.0.8 on 2020-08-23 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0003_auto_20200823_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presence',
            old_name='date',
            new_name='date_missing',
        ),
    ]
