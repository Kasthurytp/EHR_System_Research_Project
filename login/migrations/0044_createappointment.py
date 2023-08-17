# Generated by Django 4.2 on 2023-06-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0043_createdoctor_createnurse_createpatient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='createAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.BinaryField()),
                ('patient_id', models.BinaryField()),
                ('visit_type', models.BinaryField()),
                ('date', models.DateField()),
                ('location', models.BinaryField()),
                ('comments', models.BinaryField()),
            ],
        ),
    ]
