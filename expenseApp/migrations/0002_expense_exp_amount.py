# Generated by Django 4.2 on 2023-08-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='exp_amount',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
