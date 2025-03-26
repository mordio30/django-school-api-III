from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validator import validate_name_format, validate_school_email, validate_combination_format

class Student(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False,
        validators=[validate_name_format]
    )
    student_email = models.EmailField(
        null=False, blank=False, unique=True,
        validators=[validate_school_email]
    )
    personal_email = models.EmailField(
        null=True, blank=True, unique=True
    )
    locker_number = models.IntegerField(
        default=110, null=False, blank=False, unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )
    locker_combination = models.CharField(
        max_length=255, default="12-12-12", null=False, blank=False,
        validators=[validate_combination_format]
    )
    good_student = models.BooleanField(default=True)