# Generated by Django 2.0.2 on 2018-02-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('simpleticket', '0004_auto_20180219_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='value',
            field=models.IntegerField(default=1),
        ),
    ]
