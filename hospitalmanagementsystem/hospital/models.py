from django.db import models
import datetime
# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=50, null = True)
  surname = models.CharField(max_length = 45, null = True)
  middlename = models.CharField(max_length = 46, null = True)
  iIN = models.CharField(max_length=20, null = True)
  idPatient = models.CharField(max_length = 10, null = True)
  birthdate = models.DateField()
  bloodgroup = models.CharField(max_length = 5, null = True)
  email = models.EmailField(unique = True, null = True)
  gender = models.CharField(max_length = 21, null = True)
  phonenumber = models.CharField(max_length = 16, null = True)
  emergencyContact = models.CharField(max_length = 15, null = True)
  maritalstatus = models.CharField(max_length=14, null = True)
  address = models.CharField(max_length = 100, null = True)
  registration_Date = models.DateField()
  
  

  def __str__(self):
    return self.name

class Doctor(models.Model):
  name = models.CharField(max_length=50, null = True)
  surname = models.CharField(max_length=50, null = True)
  middlename = models.CharField(max_length=50, null = True)
  iIN = models.CharField(max_length=50, null = True)
  iDnumber = models.CharField(max_length = 40, null = True)
  specializationID = models.CharField(max_length=50, null = True)
  departmentID = models.CharField(max_length=50, null = True)
  experience = models.CharField(max_length=50, null = True)
  photo = models.ImageField()
  category = models.CharField(max_length=50, null = True)
  priceOftheAppointment = models.CharField(max_length=50, null = True)
  scheduleDetails = models.CharField(max_length=50, null = True)
  Degree = models.CharField(max_length=50, null = True)
  rating = models.CharField(max_length=50, null = True)
  homepageURL = models.CharField(max_length=50, null = True)
  email = models.EmailField(unique = True, null = True)
  gender = models.CharField(max_length = 20, null = True)
  phonenumber = models.CharField(max_length = 15, null = True)
  address = models.CharField(max_length = 100, null = True)
  birthdate = models.DateField()
  bloodgroup = models.CharField(max_length = 5, null = True)
  departmentID = models.CharField(max_length = 20, null = True)

  def __str__(self):
    return self.name
class Appointment(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today)
    specialization = models.CharField(max_length=30)
    doctor =models.ForeignKey(Doctor, on_delete=models.CASCADE)
    contacts = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="Pending")
    def __str__(self):
        return f"{self.name} {self.surname} doctor: {self.doctor}"