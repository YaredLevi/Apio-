# Generated by Django 3.1.4 on 2020-12-05 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201204_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candado',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.persona'),
        ),
    ]
