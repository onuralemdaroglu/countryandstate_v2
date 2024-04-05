from django.db import models

# Create your models here.
class Countries(models.Model):
    #id = models.IntegerField(primary_key=True) 
    #Django automatically appends _id to FK fields!!!
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    

class States(models.Model):
    #id = models.IntegerField(primary_key=True)
    #Django automatically appends _id to FK fields!!!
    countryId = models.ForeignKey(Countries, on_delete=models.CASCADE)
    #CASCADE: When the referenced object is deleted, also delete the objects that have references to it 
    #(when you remove a blog post for instance, you might want to delete comments as well). 
    #SQL equivalent: CASCADE.
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
