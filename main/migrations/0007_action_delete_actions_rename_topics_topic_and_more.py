# Generated by Django 4.0.5 on 2022-06-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_actions_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50, verbose_name='Person')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('discription', models.TextField(blank=True, verbose_name='Discription')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Time')),
                ('repeat', models.BooleanField(default=False, verbose_name='Repeat')),
                ('important', models.BooleanField(default=False, verbose_name='Important')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
            ],
        ),
        migrations.DeleteModel(
            name='Actions',
        ),
        migrations.RenameModel(
            old_name='Topics',
            new_name='Topic',
        ),
        migrations.AddField(
            model_name='action',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
    ]
