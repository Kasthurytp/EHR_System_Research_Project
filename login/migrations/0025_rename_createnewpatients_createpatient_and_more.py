# Generated by Django 4.2 on 2023-06-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_rename_createnewpatient_createnewpatients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='createNewPatients',
            new_name='createPatient',
        ),
        migrations.RenameField(
            model_name='createpatient',
            old_name='dob',
            new_name='dateOfBirth',
        ),
    ]
