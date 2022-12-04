from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
  doctor  = Doctor.objects.all()
  return render(request, 'index.html', {'doctor': doctor})

def appointment(request):
    doctor = Doctor.objects.order_by().values('specializationID').distinct()


    return render(request, "appointment.html", {"doctor": doctor})
def create_appointment(request,id):
    if request.method == "POST":
        doc=Doctor.objects.all()
        appointment = Appointment()
        appointment.name = request.POST.get("name")
        appointment.surname = request.POST.get("surname")
        appointment.doctor = doc[id]
        appointment.date = request.POST.get("date")
        appointment.specialization = request.POST.get("spec")
        appointment.contacts = request.POST.get("contacts")
        appointment.save()
        return HttpResponse("Your request has been sent!!!")
    else:
        return render(request,"create_appointment.html", {"pk":id})

def make_appointment(request, id):

    doctor = Doctor.objects.filter(specializationID=id).all()
    return render(request, "make_appointment.html", {"doc": doctor})

