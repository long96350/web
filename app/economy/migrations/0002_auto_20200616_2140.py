# Generated by Django 2.2.4 on 2020-06-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='chain_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='token',
            name='network_id',
            field=models.IntegerField(default=1),
        ),
    ]