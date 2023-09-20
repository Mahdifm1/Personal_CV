from django.shortcuts import render, redirect

from . import models, forms


def index(request):
    if request.method == "GET":
        person = models.Person.objects.all()[0]
        skills = models.Skills.objects.order_by('-progress_by_percent')
        portfolio = models.Portfolio.objects.all()
        work_experience = models.Work_Experience.objects.all()
        education = models.Education.objects.all()
        form = forms.ContactMeForm()

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
            'education': education,
            'form': form
        }

        return render(request, 'core/index.html', context)

    else:
        form = forms.ContactMeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = models.Contact_me(
                name=data.get('name'),
                subject=data.get('subject'),
                email=data.get('email'),
                massage=data.get('massage')
            )
            contact.save()

        return redirect('/')
