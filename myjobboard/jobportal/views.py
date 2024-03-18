from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import JobListing, Application, User
from .forms import CreateListingForm, UploadApplicationForm


@login_required
def view_applicants(request, listing_id):
    listing = JobListing.objects.get(pk=listing_id)
    applications = Application.objects.filter(job_listing=listing).order_by('-application_date')

    return render(request, "jobportal/view_applicants.html", {
        'applications' : applications
    })
    


@login_required
def close_app(request, listing_id):
    listing = JobListing.objects.get(pk=listing_id)

    if listing:

        # Update the is_active field to False
        listing.is_active = False
        # Save the object
        listing.save()

        return HttpResponseRedirect(reverse('index_succ', kwargs={'msg': 'Application is closed!'}))
    
    return HttpResponseRedirect(reverse('index_succ', kwargs={'msg': 'There was an error closing the application!'}))


def manage_jobs(request):

    # Get the user
    this_user = request.user

    # Get job listings
    listings = JobListing.objects.filter(posted_by=this_user).order_by('-posted_date')

    return render(request, "jobportal/index.html", {
        'listings' : listings
    })



def upload_application(request, listing_id):
    if request.method == 'POST':
        form = UploadApplicationForm(request.POST, request.FILES)
        job_listing = JobListing.objects.get(id=listing_id)
        
        if form.is_valid():
            application = form.save(commit=False)
            if request.user:
                form.applicant = request.user
            application.job_listing = job_listing
            application.save()
    
            return HttpResponseRedirect(reverse('index_succ', kwargs={'msg': 'Successfully Sent Application!'}))
        
    return HttpResponseRedirect(reverse('index_succ', kwargs={'msg': 'There Was an Error When Attempting to Send the Application!'}))


@login_required
def edit_job_listing(request, listing_id):
    listing = JobListing.objects.get(pk=listing_id)

    if request.method == 'POST':
        form = CreateListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_succ', kwargs={'msg': 'Update Successfull'}))
    else:
        form = CreateListingForm(instance=listing)
    return render(request, 'jobportal/edit_job_listing.html', {
        'job_form': form
    })


@login_required
def create_job_listing(request):
    if request.method == "POST":
        
        job_form = CreateListingForm(request.POST)

        if job_form.is_valid():
            job_listing = job_form.save(commit=False)
            job_listing.posted_by = request.user
            job_listing.save()

            return HttpResponseRedirect(reverse("index"))

    job_form = CreateListingForm()
    
    return render(request, "jobportal/create_job_listing.html", {
        'job_form' : job_form,
    })


def view_listing(request, listing):

    # Get job listing
    job_listing = JobListing.objects.get(id=listing)
    
    form = UploadApplicationForm()

    return render(request, "jobportal/view_listing.html", {
        'listing' : job_listing,
        'form' : form
    })


def index(request, msg=None):

    # Get job listings
    listings = JobListing.objects.order_by('-posted_date')
    
    return render(request, "jobportal/index.html", {
        'msg' : msg,
        'listings' : listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "jobportal/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "jobportal/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "jobportal/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "jobportal/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "jobportal/register.html")