# Generated by Django 2.0.2 on 2020-08-11 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_id',
        ),
    ]
