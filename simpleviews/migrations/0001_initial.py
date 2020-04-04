# Generated by Django 3.0.5 on 2020-04-04 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 4, 4, 2, 58, 15, 876325))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 4, 4, 2, 58, 15, 876029))),
                ('last_seen', models.DateTimeField()),
            ],
        ),
    ]
