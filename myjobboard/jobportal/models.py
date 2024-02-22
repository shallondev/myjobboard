from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    pass


class JobListing(models.Model):
    position_title = models.CharField(max_length=64, unique=False)
    company = models.CharField(max_length=100, unique=False)
    city = models.CharField(max_length=64, unique=False, blank=True, null=True)
    province_state = models.CharField(max_length=64, unique=False, blank=True, null=True)
    country = models.CharField(max_length=64, unique=False, blank=True, null=True)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
    is_active = models.BooleanField(default=True)
    logo_url = models.URLField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.BinaryField(blank=True, null=True)
    resume = models.BinaryField(blank=True, null=True)
    first_name = models.CharField(max_length=64, unique=False)
    middle_name = models.CharField(max_length=64, unique=False)
    last_name = models.CharField(max_length=64, unique=False)
    email = models.EmailField(unique=False)
    annual_salary = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(1000000)])