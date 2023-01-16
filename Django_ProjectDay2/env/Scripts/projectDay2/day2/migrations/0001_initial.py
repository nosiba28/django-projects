# Generated by Django 4.1.1 on 2022-11-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('emp_name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=150)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]