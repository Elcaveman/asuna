# Generated by Django 3.2.4 on 2021-06-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210622_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='client_name',
            field=models.CharField(blank=True, help_text='150 characters or fewer.', max_length=150, null=True, verbose_name='Patient name'),
        ),
    ]
