# Generated by Django 4.2.3 on 2023-08-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('unknown', "I don't want to share")], max_length=30, null=True),
        ),
    ]
