# Generated by Django 4.2 on 2023-06-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_createnewpatient_dob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='createNewPatient',
            new_name='createNewPatients',
        ),
    ]
