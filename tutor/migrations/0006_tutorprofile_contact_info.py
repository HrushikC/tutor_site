# Generated by Django 3.0.7 on 2020-07-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0005_changeDefaultRating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorprofile',
            name='contact_info',
            field=models.TextField(default='Text or Call 555-555-5555'),
        ),
    ]
