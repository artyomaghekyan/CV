from django.shortcuts import render, HttpResponse
from .models import Profile
import pdfkit
import io
from django.template import loader
from django.conf.urls import handler404

handler404 = 'django.views.defaults.page_not_found'


# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        experience = request.POST.get('experience','')
        skills = request.POST.get('skills','')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, 
        degree=degree, school=school, university=university, experience=experience, skills=skills)
        profile.save()
        context ={'profile': profile}
        return render(request, 'cvapp/forms.html',  context)
    else:
        return render(request, 'cvapp/forms.html')

def cv(request, id):
    user_profile = Profile.objects.get(id=id)
    context = {'id': user_profile}
    template = loader.get_template('cvapp/cv.html')
    html = template.render(context)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    config = pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
 
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
 
    response['Content-Disposition'] ='attachment;filename=resume.pdf'
 
    return response


def cv_list(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'cvapp/cv_list.html', context)