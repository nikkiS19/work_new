# Generated by Django 2.0.2 on 2020-08-12 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor_new', '0002_content_file_text_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
