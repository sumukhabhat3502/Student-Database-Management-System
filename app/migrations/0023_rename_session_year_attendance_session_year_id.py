# Generated by Django 4.1.2 on 2022-12-27 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_session_year_id_attendance_session_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='session_year',
            new_name='session_year_id',
        ),
    ]
