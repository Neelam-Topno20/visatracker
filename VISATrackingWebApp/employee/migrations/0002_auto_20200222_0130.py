# Generated by Django 3.0.3 on 2020-02-21 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationhistory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 990536), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 991536), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 988537), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 988537), verbose_name='date modified'),
        ),
        migrations.AlterField(
            model_name='visaappplication',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 990536), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='visaappplication',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 30, 9, 990536), verbose_name='date modified'),
        ),
    ]
