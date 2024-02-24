from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import JobListing
from .forms import CreateListingForm


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

    return render(request, "jobportal/view_listing.html", {
        'listing' : job_listing
    })


def index(request):

    # Get job listings
    listings = JobListing.objects.order_by('-posted_date')
    
    return render(request, "jobportal/index.html", {
        'listings' : listings
    })
