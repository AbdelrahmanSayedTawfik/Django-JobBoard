from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE, default='Full Time')
    description = models.TextField(default='')
    published_at = models.DateTimeField(auto_now=True)
    vacency = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experance = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title