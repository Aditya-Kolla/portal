# Generated by Django 2.0.9 on 2018-12-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_gamesessionplayersignup_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesession',
            name='report_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Reporting time'),
        ),
    ]
