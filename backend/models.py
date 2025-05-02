from django.db import models

class SchoolParams(models.Model):
    school_id = models.CharField(max_length=200) #share id with school
    acceptance_rate = models.FloatField()
    tuition = models.IntegerField() #in US cents $10.51 = 1051

    def __str__(self):
        return self.school_id



class School(models.Model):
    #school basic data
    school_id = models.CharField(max_length=200) #share id with school params
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300, blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.school_id

