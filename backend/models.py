from __future__ import annotations

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator, RegexValidator, ValidationError
)
from django.utils.deconstruct import deconstructible
from django_countries.fields import CountryField  # pip install django-countries


@deconstructible
class StepValidator:
    """
    Ensure that a numeric value is a multiple of `step`.
    """
    def __init__(self, step):
        self.step = step

    def __call__(self, value):
        # we multiply then mod 1 to allow floats
        if (value / self.step) % 1 != 0:
            raise ValidationError(f"Value must be in steps of {self.step}.")

    def __eq__(self, other):
        return isinstance(other, StepValidator) and other.step == self.step

class Major(models.TextChoices):
    ENGINEERING = "ENG", "Engineering"
    MATH         = "MTH", "Mathematics"
    PHYSICS      = "PHY", "Physics"
    CHEMISTRY    = "CHM", "Chemistry"
    BIOLOGY      = "BIO", "Biology"
    ENGLISH      = "ENGG", "English"
    HISTORY      = "HIS", "History"
    # …add your full list of intended majors…

class Gender(models.TextChoices):
    MALE   = "M", "Male"
    FEMALE = "F", "Female"
    OTHER  = "O", "Other / Prefer not to say"


class UserProfile(models.Model):
    user = models.OneToOneField(
        "FrontendUser",
        on_delete=models.CASCADE,
        related_name="profile"
    )

    # SAT reading & math: integers 200–800 in steps of 10
    sat_reading = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(200),
            MaxValueValidator(800),
            StepValidator(10),
        ],
        help_text="SAT Reading score, 200–800 in 10‑point increments"
    )
    sat_math = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(200),
            MaxValueValidator(800),
            StepValidator(10),
        ],
        help_text="SAT Math score, 200–800 in 10‑point increments"
    )

    # GPA: decimal 0.00–4.00 in steps of 0.05
    gpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(4.00),
            StepValidator(0.05),
        ],
        help_text="GPA on a 0.00–4.00 scale in 0.05 increments"
    )

    # Intended major: choice field
    intended_major = models.CharField(
        max_length=4,
        choices=Major.choices,
        default=Major.ENGINEERING,
        help_text="Intended college major"
    )

    # Recommendation strength: integer 1–4
    recommendation_strength = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4),
        ],
        help_text="How strong the recommendation is (1–4)"
    )

    # Nationality: using django‑countries for ISO country codes
    nationality = CountryField(
        blank_label="(Select country)",
        blank=True,
        null=True,
        help_text="Country of nationality"
    )

    # Gender: simple choice field
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
        help_text="Gender identity"
    )

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



