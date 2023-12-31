# Generated by Django 4.2 on 2023-06-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0046_rename_createnewappointment_createappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='createPrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id_num', models.BinaryField()),
                ('patient_id_num', models.BinaryField()),
                ('patientName', models.BinaryField()),
                ('date', models.DateField()),
                ('medicationName', models.BinaryField()),
                ('dose', models.BinaryField()),
                ('frequency', models.BinaryField()),
                ('encryption_key', models.BinaryField()),
            ],
        ),
    ]
