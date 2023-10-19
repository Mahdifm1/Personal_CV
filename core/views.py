import mimetypes
from pathlib import Path

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

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
            # save contact me form
            data = form.cleaned_data
            contact = models.Contact_me(
                name=data.get('name'),
                subject=data.get('subject'),
                email=data.get('email'),
                massage=data.get('massage')
            )
            contact.save()

            # send email to site admin
            message = render_to_string('core/contact_me.html', context={
                'name': data.get('name'),
                'subject': data.get('subject'),
                'email': data.get('email'),
                'massage': data.get('massage')
            })
            send_mail('Someone is trying to hire you!'.title(), message, 'sender email address',
                      ['admin email address'], fail_silently=False, html_message=message)

        return redirect('/')


def download_cv(request):
    person = models.Person.objects.all().first()
    cv = None
    if person:
        cv = person.personal_cv_pdf

    fl_path = ""
    filename = ""
    if not cv:
        # fill these variables with real values
        fl_path = str(Path(__file__).resolve().parent.parent) + '/files/cv.pdf'
        print(fl_path)
        filename = 'cv.pdf'

    else:
        filename = person.personal_cv_pdf.name.split('/')[-1]
        fl_path = person.personal_cv_pdf.path

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
