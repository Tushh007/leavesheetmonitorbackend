# Generated by Django 2.2.3 on 2019-07-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=9)),
                ('day_type', models.CharField(max_length=20)),
            ],
        ),
    ]