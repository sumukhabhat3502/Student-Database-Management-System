# Generated by Django 4.1.2 on 2022-10-25 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
