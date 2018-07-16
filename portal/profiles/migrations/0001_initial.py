# Generated by Django 2.0.6 on 2018-07-16 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='Class Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterFaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='Faction Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterRace',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='Race Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DMNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.TextField(verbose_name='Note on player')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Character name')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.CharacterFaction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dci', models.IntegerField(blank=True, null=True, verbose_name='DCI')),
                ('role', models.CharField(default='player', max_length=20, verbose_name='Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='pc_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.CharacterClass'),
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.CharacterRace'),
        ),
        migrations.AddField(
            model_name='dmnote',
            name='dm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_notes_given', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='dmnote',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_notes', to='profiles.Profile'),
        ),
    ]
