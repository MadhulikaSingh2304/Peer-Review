# Generated by Django 4.2.1 on 2023-05-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('batch', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('guide', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0)),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerapp.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerapp.team'),
        ),
    ]
