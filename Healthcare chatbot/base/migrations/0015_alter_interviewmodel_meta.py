# Generated by Django 3.2.4 on 2021-06-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20210627_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewmodel',
            name='meta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.interviewmetadatamodel', verbose_name='Interview Metadata'),
        ),
    ]