# Generated by Django 4.2.4 on 2023-09-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('role', models.CharField(max_length=250)),
            ],
        ),
    ]
