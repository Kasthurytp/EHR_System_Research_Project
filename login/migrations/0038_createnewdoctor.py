# Generated by Django 4.2 on 2023-06-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0037_createnewpatient_delete_newcreatepatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='createNewDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pics')),
                ('first_name', models.BinaryField()),
                ('last_name', models.BinaryField()),
                ('dob', models.DateField()),
                ('sex', models.BinaryField()),
                ('nic', models.BinaryField()),
                ('password', models.BinaryField()),
                ('mobile_number', models.BinaryField()),
                ('email', models.BinaryField()),
                ('address', models.BinaryField()),
                ('primary_phone', models.BinaryField()),
                ('secondary_phone', models.BinaryField()),
                ('encryption_key', models.BinaryField()),
            ],
        ),
    ]
