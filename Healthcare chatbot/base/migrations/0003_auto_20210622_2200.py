# Generated by Django 3.2.3 on 2021-06-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_interviewmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewmodel',
            name='questions',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='interviewmodel',
            name='results',
            field=models.JSONField(null=True),
        ),
    ]
