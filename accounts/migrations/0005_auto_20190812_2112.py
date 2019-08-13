# Generated by Django 2.2.4 on 2019-08-12 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0005_auto_20190809_0022'),
        ('accounts', '0004_remove_user_realname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='video',
            field=models.ManyToManyField(to='beauty.Video'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(default=datetime.datetime(2019, 8, 12, 21, 12, 57, 501089)),
        ),
    ]