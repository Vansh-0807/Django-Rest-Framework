from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 1000)
    fees = models.IntegerField(default = 5000000)

class Color(models.Model):
    color_name = models.CharField(max_length = 100)

    def __str__(self) ->str:
        return self.color_name
    
class Person(models.Model):
    name = models.CharField(max_length = 100)
    #added foreign key
    color = models.ForeignKey(Color, on_delete = models.CASCADE, null = True, blank = True,  related_name = "color")
    # on_delete = models.CASCADE tells what happens when the Color is deleted, null =  true means it can be empty in the database, blank = True means it can be empty in forms 
    age = models.IntegerField()
    gender = models.CharField(default = 'NA')

    def __str__(self) ->str:
        return self.name
    