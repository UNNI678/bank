from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=280)
    img=models.ImageField(upload_to='clicks')
    desc=models.TextField()

    def __str__(self):
        return self.name
