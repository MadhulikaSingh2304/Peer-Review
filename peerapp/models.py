from django.db import models
from django.core.validators import MaxValueValidator


class Team(models.Model):
    batch = models.CharField(max_length=100, primary_key=True)
    domain = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    guide = models.CharField(max_length=100)
    
    def __str__(self):
        return self.batch
    

class Person(models.Model):
    batch = models.ForeignKey(Team, on_delete=models.CASCADE)
    usn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.usn)

class Rating(models.Model):
    usn = models.ForeignKey(Person, on_delete=models.CASCADE, to_field='usn')
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(15)])
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return str(self.usn)

