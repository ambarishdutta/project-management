# Generated by Django 3.0.7 on 2021-05-25 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210525_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskwork',
            name='date_added',
        ),
        migrations.AddField(
            model_name='taskwork',
            name='datecomp',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]