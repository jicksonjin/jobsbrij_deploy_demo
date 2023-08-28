from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class job_category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class job_details(models.Model):
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    expiry_on=models.DateField()

    job_description=RichTextField(null=True,blank=True)
    how_to_apply=RichTextField(null=True,blank=True)
    cat=models.ForeignKey(job_category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="jobs")
    def __str__(self):
        f=f"{self.job_title} on {self.company_name}"
        return f