# Generated by Django 4.1.2 on 2022-12-27 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_attendance_session_year_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='session_year_id',
            new_name='session_year',
        ),
    ]