from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=50,default="Shakaib Hassan")
    email = models.CharField(max_length=50,default="shakaibhassan16@gmail.com")
    
    def __str__(self):
        return self.full_name


class Articles(models.Model):
    time_choices =[ 
    ("5", "5 min"), 
    ("10", "10 min"), 
    ("15", "15 min"), 
    ("20", "20 min"), 
    ("25", "25 min"), 
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/')
    name = models.TextField()
    published_date = models.DateField()
    time_read = models.CharField(max_length=10,choices = time_choices)
    content = models.TextField()

    def __str__(self):
        return self.name
