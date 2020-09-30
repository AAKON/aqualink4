from django.db import models

# Create your models here.
class Career_description (models.Model):
    work_f_home = 'Work from Home'
    work_a_office = 'Work at Office'
    full_time = 'FUll Time'
    part_time = 'Part Time'
    contractual = 'Contractual'
    
    WORK_PLACE_CHOICES = [
        (work_f_home, 'Work from Home'),
        (work_a_office, 'Work at Office'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        (full_time, 'FUll Time'),
        (part_time, 'Part Time'),
        (contractual, 'Contractual'),
    ]

    designation = models.CharField(max_length=200)
    vacancy = models.IntegerField(default=None,null=True)
    job_responsibility = models.TextField()
    employment_status = models.CharField(max_length=50,default=full_time,choices=EMPLOYMENT_STATUS_CHOICES)
    work_place = models.CharField(max_length=50,default=work_f_home,choices=WORK_PLACE_CHOICES)
    education = models.TextField()
    experience = models.CharField(max_length=500)
    additional_requirment = models.TextField()
    job_location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.designation
