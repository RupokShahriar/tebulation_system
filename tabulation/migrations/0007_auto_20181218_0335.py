# Generated by Django 2.1.4 on 2018-12-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0006_student_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemarks',
            name='obtained_marks',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='labmarks',
            name='obtained_marks',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='theorymarks',
            name='obtained_marks',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
