# Generated by Django 4.0.2 on 2022-02-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('dinner', 'شام'), ('lunch', 'ناهار'), ('drinks', 'نوشیدنی')], default='dinner', max_length=10),
        ),
    ]
