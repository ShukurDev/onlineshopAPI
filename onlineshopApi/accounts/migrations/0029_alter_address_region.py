# Generated by Django 4.0.1 on 2022-01-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_address_region_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Surxondaryo', 'Surxondaryo'), ('Samarqand', 'Samarqand'), ('Jizzax', 'Jizzax'), ('Toshkent', 'Toshkent:'), ('Fargona', 'Fargona'), ('Toshkent vil', 'Toshkent vil'), ('Qashqadaryo', 'Qashqadaryo'), ('Xorazm', 'Xorazm'), ('Navoi', 'Navoi'), ('Andijon', 'Andijon'), ('Buxoro', 'Buxoro'), ('Namangan', 'Namangan')], default='empty', max_length=100),
        ),
    ]
