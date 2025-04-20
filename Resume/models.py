from django.db import models
import datetime
# Create your models here.
class BasicDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    summary = models.TextField()
    linkedin = models.URLField()
    github = models.URLField()
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
class Experince(models.Model):
    user = models.ForeignKey(BasicDetails, on_delete=models.CASCADE, related_name="experiences")
    title = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    startdate = models.DateField(default = datetime.date.today)
    enddate = models.DateField(null = True, blank = True)
    location = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    description = models.TextField()
    skills_used = models.CharField(max_length=100)
    def __str__(self):
        return self.organization
    
    
class Project(models.Model):
    project_title = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField(null=True, blank=True)
    project_details = models.TextField()
    
    
    
        
class Skills(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    course_type = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    grading_system = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places = 2)
    
    def __str__(self):
       return self.degree
   
class Certifications(models.Model):
    certificate_name = models.CharField(max_length=100)
    certification_id = models.CharField(max_length=100)
    certification_url = models.URLField()
    
    def __str__(self):
        return self.certificate_name