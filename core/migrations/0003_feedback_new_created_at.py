# Generated by Django 3.0.2 on 2020-01-16 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200116_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_new',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 1, 1, 12, 00, 00, 0, tzinfo=utc)),
            preserve_default=False,
        ),
    ]