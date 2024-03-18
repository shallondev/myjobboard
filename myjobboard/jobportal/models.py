from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass


class JobListing(models.Model):
    """
    Holds job postings
    """
    # Basic job information fields
    position_title = models.CharField(max_length=64, unique=False)
    company = models.CharField(max_length=100, unique=False)
    city = models.CharField(max_length=64, unique=False, blank=True, null=True)
    province_state = models.CharField(max_length=64, unique=False, blank=True, null=True)
    country = models.CharField(max_length=64, unique=False)
    
    # Information regarding post using RichTextField
    summary = RichTextField()  
    responsibilities = RichTextField(null=True, blank=True)  
    must_have = RichTextField(blank=True, null=True)  
    qualifications = RichTextField(blank=True, null=True)  
    bonus_skills = RichTextField(null=True, blank=True)  

    # Other job details
    employment_type = models.CharField(max_length=100, unique=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
    annual_salary = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(1000000)], null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    logo_url = models.URLField(blank=True, null=True, max_length=500)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position_title} at {self.company}"


class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='applications', blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)

    # PDF
    cover_letter = models.FileField(upload_to='pdfs/cover_letters', default='txt.pdf', blank=True, null=True)
    resume = models.FileField(upload_to='pdfs/resumes', default='txt.pdf')

    # Information
    first_name = models.CharField(max_length=64, unique=False)
    middle_name = models.CharField(max_length=64, unique=False, blank=True, null=True)
    last_name = models.CharField(max_length=64, unique=False)
    email = models.EmailField(unique=False)

    def __str__(self):
        return f"Application for {self.job_listing.position_title} by {self.first_name, self.last_name}"
    
    def get_resume_url(self):
        return self.resume.url
    
    def get_cover_letter_url(self):
        return self.cover_letter.url