# Generated by Django 4.1.2 on 2022-10-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
