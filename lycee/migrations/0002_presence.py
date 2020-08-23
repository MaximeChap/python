# Generated by Django 3.0.8 on 2020-08-23 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='date of the day')),
                ('isMissing', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Student')),
            ],
        ),
    ]
