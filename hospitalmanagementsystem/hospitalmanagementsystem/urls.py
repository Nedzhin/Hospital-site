from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path("appointment/", appointment, name="appointment"),
    path("create_appointment/<int:id>/", create_appointment, name="create_appointment"),
    path("make_appointment/<str:id>/", make_appointment, name="make_appointment"),
    path("make_appointment_post/", make_appointment_post, name="make_appointment_post")
]
