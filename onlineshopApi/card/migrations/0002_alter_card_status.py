# Generated by Django 4.0.1 on 2022-01-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(blank=True, choices=[('approved', 'approved'), ('Waiting', 'Waiting'), ('New', 'New')], max_length=80, null=True),
        ),
    ]