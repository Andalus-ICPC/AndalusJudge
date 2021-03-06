# Generated by Django 2.0.7 on 2021-03-30 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='user',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_active': True, 'role__short_name': 'contestant'}, to=settings.AUTH_USER_MODEL),
        ),
    ]
