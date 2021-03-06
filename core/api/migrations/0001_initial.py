# Generated by Django 3.1.4 on 2020-12-05 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('saldo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Candado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('altitud', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.persona')),
            ],
        ),
    ]
