# Generated by Django 5.0.6 on 2024-05-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]