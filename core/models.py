from django.db import models
from solo.models import SingletonModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    # person name
    name = models.CharField(max_length=50)
    # 3 top skill separated by , like WEB DEVELOPER, GRAPHIC DESIGNER, PHOTOGRAPHER
    short_skills = models.TextField(max_length=100)
    # about me field
    about = models.TextField()

    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    languages = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image')


class Skills(models.Model):
    skill_name = models.CharField(max_length=30)
    progress_by_percent = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)

