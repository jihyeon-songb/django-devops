# Generated by Django 4.0 on 2021-12-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='line',
            field=models.BooleanField(default=False),
        ),
    ]
