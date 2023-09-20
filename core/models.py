from django.db import models
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

    telegram_url = models.CharField(max_length=50)
    email_url = models.CharField(max_length=50)
    linkedin_url = models.CharField(max_length=50)
    github_url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    skill_name = models.CharField(max_length=30)
    progress_by_percent = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.skill_name


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='portfolio_images')
    url = models.URLField(max_length=200)
    person = models.ForeignKey(Person, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Work_Experience(models.Model):
    company_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    university_name = models.CharField(max_length=20)
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.university_name


class Contact_me(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()
    is_read_by_admin = models.BooleanField(default=False)
