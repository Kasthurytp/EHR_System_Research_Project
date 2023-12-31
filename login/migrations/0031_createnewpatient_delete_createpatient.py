# Generated by Django 4.2 on 2023-06-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0030_auto_20230613_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='createNewPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pics')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('nic', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('primary_phone', models.CharField(max_length=15)),
                ('secondary_phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='createPatient',
        ),
    ]
