# Generated by Django 2.0.9 on 2018-12-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20181220_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dci',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='DCI'),
        ),
    ]