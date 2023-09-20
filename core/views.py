from django.shortcuts import render
from . import models


def index(request):
    if request.method == "GET":
        person = models.Person.objects.all()[0]
        skills = models.Skills.objects.order_by('-progress_by_percent')
        portfolio = models.Portfolio.objects.all()
        work_experience = models.Work_Experience.objects.all()
        education = models.Education.objects.all()

        separated_skills = []
        skill_row = []
        for i in range(len(skills)):
            skill_row.append(skills[i])
            if (i + 1) % 2 == 0:
                separated_skills.append(skill_row)
                skill_row = []


        context = {
            'person': person,
            'portfolio': portfolio,
            'skills': separated_skills,
            'work_experience': work_experience,
            'education': education
        }

        return render(request, 'core/index.html', context)

    else:
        return
