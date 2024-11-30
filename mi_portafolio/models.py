from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=200)  
    company = models.CharField(max_length=200)  
    start_date = models.DateField() 
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField()  

    def __str__(self):
        return f"{self.title} at {self.company}"
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='media/projects/images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Education(models.Model):
    title = models.CharField(max_length=200)  
    place_studies = models.CharField(max_length=200) 
    start_date = models.DateField() 
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField()  
    def __str__(self):
        return f"{self.title} at {self.place_studies}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name