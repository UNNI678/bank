from django.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    # dob=models.DateField(auto_now=True)
    # age=models.IntegerField()
    # mob_num=models.CharField()
    # gender=models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')])
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name