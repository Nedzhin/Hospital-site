# Generated by Django 3.2.7 on 2022-12-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_rename_specalization_appointment_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
