# Generated by Django 2.1.2 on 2018-12-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20181204_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote',
            field=models.PositiveIntegerField(default=0, verbose_name='Голос'),
        ),
    ]