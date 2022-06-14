# Generated by Django 4.0.2 on 2022-02-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
