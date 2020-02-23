# Generated by Django 3.0.3 on 2020-02-21 19:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 585279), verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 583280), verbose_name='date created')),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 583280), verbose_name='date modified')),
                ('manager_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VisaAppplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 585279), verbose_name='date created')),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 585279), verbose_name='date modified')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ApplicationStatus')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ManyToManyField(to='employee.Role'),
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 2, 22, 1, 25, 27, 586279), verbose_name='date created')),
                ('application_history_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.ApplicationHistory')),
            ],
        ),
        migrations.CreateModel(
            name='EmailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('status_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.ApplicationStatus')),
            ],
        ),
        migrations.AddField(
            model_name='applicationhistory',
            name='application_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ApplicationStatus'),
        ),
    ]