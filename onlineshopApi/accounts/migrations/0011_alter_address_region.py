# Generated by Django 3.2 on 2022-01-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220113_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Xorazm', 'Xorazm'), ('Namangan', 'Namangan'), ('Samarqand', 'Samarqand'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxondaryo', 'Surxondaryo'), ('Toshkent', 'Toshkent:'), ('Navoi', 'Navoi'), ('Andijon', 'Andijon')], default='empty', max_length=100),
        ),
    ]
