# Generated by Django 2.1.4 on 2018-12-17 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0005_thesisconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default='2015', max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='batch'),
            preserve_default=False,
        ),
    ]
