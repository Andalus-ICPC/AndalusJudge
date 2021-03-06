# Generated by Django 2.0.7 on 2021-04-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeserver', '0002_auto_20210401_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judgeserver',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='judgeserver',
            name='port',
        ),
        migrations.AddField(
            model_name='judgeserver',
            name='address',
            field=models.CharField(default='null', max_length=1200),
        ),
        migrations.AddField(
            model_name='judgeserver',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
