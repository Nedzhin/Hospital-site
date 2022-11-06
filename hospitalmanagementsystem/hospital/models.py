from django.db import models

# Create your models here.

class Patient(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique = True)
  gender = models.CharField(max_length = 20)
  phonenumber = models.CharField(max_length = 15)
  address = models.CharField(max_length = 100)
  birthdate = models.DateField()
  bloodgroup = models.CharField(max_length = 5)

  def __str__(self):
    return self.name

class Doctor(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique = True)
  gender = models.CharField(max_length = 20)
  phonenumber = models.CharField(max_length = 15)
  address = models.CharField(max_length = 100)
  birthdate = models.DateField()
  bloodgroup = models.CharField(max_length = 5)
  departmentID = models.CharField(max_length = 20)

  def __str__(self):
    return self.name


