# Generated by Django 3.2.4 on 2021-06-26 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_interviewmodel_interview_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewMetadataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('is_smoker', models.BooleanField(verbose_name='Smoker')),
                ('is_pregnant', models.BooleanField(verbose_name='Pregnant')),
                ('is_obese', models.BooleanField(verbose_name='Obese')),
                ('is_injured', models.BooleanField(verbose_name='Injured')),
                ('has_hypertension', models.BooleanField(verbose_name='Hypertension')),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Symptom name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='interviewmodel',
            options={'ordering': ['creation_date']},
        ),
        migrations.RemoveField(
            model_name='interviewmodel',
            name='questions',
        ),
        migrations.CreateModel(
            name='Paterns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200, verbose_name='Symptom Wording(patern)')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.symptoms', verbose_name='Symptom')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(choices=[('I', 'Incomming'), ('O', 'Outgoing')], max_length=1)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chathistory', verbose_name='Chat History')),
            ],
        ),
        migrations.CreateModel(
            name='Desease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Desease name')),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('is_smoker', models.BooleanField(verbose_name='Smoker')),
                ('is_pregnant', models.BooleanField(verbose_name='Pregnant')),
                ('is_obese', models.BooleanField(verbose_name='Obese')),
                ('is_injured', models.BooleanField(verbose_name='Injured')),
                ('has_hypertension', models.BooleanField(verbose_name='Hypertension')),
                ('symptoms', models.ManyToManyField(to='base.Symptoms', verbose_name='Symptoms')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='chathistory',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.interviewmodel', verbose_name='interview'),
        ),
    ]