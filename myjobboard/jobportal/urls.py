from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jobs/<str:listing>", views.view_listing, name="view_listing"),
    path("create_job_listing", views.create_job_listing, name="create_job_listing"),
]