# Generated by Django 5.0.6 on 2024-05-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_app', '0003_remove_notes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.CharField(max_length=250, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]