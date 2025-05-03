from django.db import models
from django.contrib.auth.models import AbstractUser

class FrontendUser(AbstractUser):
    # username, email, password already inherited
    username = models.CharField(
        max_length=30,
        unique=True,
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    biography       = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

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
    description = models.TextField(blank=True)

    def __str__(self):
        return self.school_id



