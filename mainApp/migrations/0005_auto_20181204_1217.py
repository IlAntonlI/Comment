# Generated by Django 2.1.2 on 2018-12-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20181203_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]