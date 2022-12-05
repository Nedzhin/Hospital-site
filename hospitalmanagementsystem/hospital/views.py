from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
  doctor  = Doctor.objects.all()
  return render(request, 'index.html', {'doctor': doctor})

def appointment(request):
    doc = Doctor.objects.order_by().values('specializationID').distinct()
    doctor = Doctor.objects.all()
    apppoint = Appointment.objects.all()
    return render(request, "appointment.html", {"doctor": doctor,'doc':doc, "appo":apppoint})

def create_appointment(request,id):
    if request.method == "POST":
        doc=Doctor.objects.get(pk=id)
        appointment = Appointment()
        appointment.name = request.POST.get("name")
        appointment.surname = request.POST.get("surname")
        appointment.doctor = doc
        appointment.date = request.POST.get("date")
        appointment.specialization = request.POST.get("spec")
        appointment.contacts = request.POST.get("contacts")
        appointment.save()
        return HttpResponseRedirect("/appointment/")
    else:

        return render(request,"create_appointment.html", {"pk":id})

def make_appointment(request, id):
    doctor = Doctor.objects.filter(specializationID=id).all()
    return render(request, "make_appointment.html", {"doc": doctor})

def make_appointment_post(request):

    doctor = Doctor.objects.filter(Q(name__contains=request.POST.get("subs")) | Q(specializationID__contains=request.POST.get("subs")))
    return render(request, "make_appointment.html", {"doc": doctor})
