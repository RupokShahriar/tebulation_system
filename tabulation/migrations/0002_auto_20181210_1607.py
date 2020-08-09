# Generated by Django 2.1.4 on 2018-12-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AttendanceMakrs',
            new_name='AttendanceMarks',
        ),
        migrations.AddField(
            model_name='prerequisite',
            name='discipline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tabulation.Discipline'),
            preserve_default=False,
        ),
    ]
