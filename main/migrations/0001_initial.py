# Generated by Django 4.0.5 on 2022-06-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
