# Generated by Django 4.1.2 on 2022-12-27 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_session_year_attendance_session_year_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='session_year_id',
        ),
    ]
