from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Tanu"),
    path("about/",views.about, name="about"),
    path("services/",views.services, name="services"),
    path("contact/",views.contact, name="contact"),
]
