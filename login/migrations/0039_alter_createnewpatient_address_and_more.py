# Generated by Django 4.2 on 2023-06-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0038_createnewdoctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewpatient',
            name='address',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='email',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='last_name',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='mobile_number',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='nic',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='password',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='primary_phone',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='secondary_phone',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='createnewpatient',
            name='sex',
            field=models.BinaryField(),
        ),
    ]
