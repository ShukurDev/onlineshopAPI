# Generated by Django 3.2 on 2022-01-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220113_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[(2, 'Surxondaryo'), (1, 'Toshkent:'), (7, 'Qashqadaryo'), (8, 'Xorazm'), (5, 'Navoi'), (3, 'Andijon'), (4, 'Namangan'), (12, 'Buxoro'), (6, 'Samarqand'), (9, 'Fargona'), (10, 'Jizzax'), (11, 'Toshkent vil')], default='empty', max_length=100),
        ),
    ]
