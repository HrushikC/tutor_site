# Generated by Django 3.0.7 on 2020-06-28 20:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='TutorProfile',
        ),
        migrations.RenameField(
            model_name='tutorprofile',
            old_name='content',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='tutorprofile',
            old_name='title',
            new_name='name',
        ),
    ]
