# Generated by Django 2.2.17 on 2021-04-13 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0121_merge_20210410_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='code',
            field=models.CharField(help_text='A short, unique code for the problem, used in the url after /problem/', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9_]+$', 'Problem code must be ^[a-z0-9_]+$')], verbose_name='problem code'),
        ),
    ]
