# Generated by Django 4.2.16 on 2024-11-28 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='education',
            table='Education',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='Employee',
        ),
        migrations.AlterModelTable(
            name='office',
            table='Office',
        ),
    ]
