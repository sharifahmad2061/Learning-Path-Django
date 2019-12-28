from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=150)
    employer = models.CharField(max_length=150, null=True)
    focal_person = models.CharField(max_length=50, null=True)
    focal_person_contact = models.CharField(max_length=30, null=True)
    focal_person_email = models.EmailField(null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.TextField()
