from django.db import models

class SchoolParams(models.Model):
    school_id = models.CharField(max_length=200) #share id with school
    acceptance_rate = models.FloatField()
    tuition = models.IntegerField() #in US cents $10.51 = 1051

    def __str__(self):
        return self.id



class School(models.Model):
    #school basic data
    name = models.CharField(max_length=200)
    school_id = models.CharField(max_length=200) #share id with school params

    def __str__(self):
        return self.id

