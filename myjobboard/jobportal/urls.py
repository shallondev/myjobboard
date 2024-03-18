from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/<str:msg>", views.index, name="index_succ"),
    path("jobs/<str:listing>", views.view_listing, name="view_listing"),
    path("create_job_listing", views.create_job_listing, name="create_job_listing"),
    path('upload_application/<int:listing_id>', views.upload_application, name='upload_application'),
    path("manage_jobs", views.manage_jobs, name="manage_jobs"),
    path("edit_job_listing/<int:listing_id>", views.edit_job_listing, name="edit_job_listing"),
    path("close_app/<int:listing_id>", views.close_app, name="close_app"),
    path("view_applicants/<int:listing_id>", views.view_applicants, name="view_applicants"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
