# Generated by Django 4.1.4 on 2023-02-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_pertask_kwargs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertask',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pertask',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]