# Generated by Django 2.1.2 on 2018-12-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20181204_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
