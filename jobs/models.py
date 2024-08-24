from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skills_required = models.TextField(null=True, blank=True)
    experience_required = models.CharField(max_length=255, null=True, blank=True)
    education_required = models.CharField(max_length=255, null=True, blank=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.CharField(max_length=255, blank=True, null=True)
    job_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company_name} ({self.location})"