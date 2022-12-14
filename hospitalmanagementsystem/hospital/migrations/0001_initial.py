# Generated by Django 3.2.16 on 2022-11-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('surname', models.CharField(max_length=50, null=True)),
                ('middlename', models.CharField(max_length=50, null=True)),
                ('iIN', models.CharField(max_length=50, null=True)),
                ('iDnumber', models.CharField(max_length=40, null=True)),
                ('specializationID', models.CharField(max_length=50, null=True)),
                ('experience', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=50, null=True)),
                ('priceOftheAppointment', models.CharField(max_length=50, null=True)),
                ('scheduleDetails', models.CharField(max_length=50, null=True)),
                ('Degree', models.CharField(max_length=50, null=True)),
                ('rating', models.CharField(max_length=50, null=True)),
                ('homepageURL', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5, null=True)),
                ('departmentID', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('surname', models.CharField(max_length=45, null=True)),
                ('middlename', models.CharField(max_length=46, null=True)),
                ('iIN', models.CharField(max_length=20, null=True)),
                ('idPatient', models.CharField(max_length=10, null=True)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('gender', models.CharField(max_length=21, null=True)),
                ('phonenumber', models.CharField(max_length=16, null=True)),
                ('emergencyContact', models.CharField(max_length=15, null=True)),
                ('maritalstatus', models.CharField(max_length=14, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('registration_Date', models.DateField()),
            ],
        ),
    ]
