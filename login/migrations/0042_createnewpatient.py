# Generated by Django 4.2 on 2023-06-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0041_delete_createnewpatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='createNewPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pics')),
                ('first_name', models.BinaryField()),
                ('last_name', models.BinaryField()),
                ('dob', models.DateField()),
                ('sex', models.BinaryField()),
                ('nic', models.BinaryField()),
                ('mobile_number', models.BinaryField()),
                ('email', models.BinaryField()),
                ('address', models.BinaryField()),
                ('primary_phone', models.BinaryField()),
                ('secondary_phone', models.BinaryField()),
                ('encryption_key', models.BinaryField()),
            ],
        ),
    ]
