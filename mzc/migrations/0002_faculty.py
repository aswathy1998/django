# Generated by Django 2.1.3 on 2019-10-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mzc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fno', models.CharField(max_length=10)),
                ('Designation', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=20)),
            ],
        ),
    ]
