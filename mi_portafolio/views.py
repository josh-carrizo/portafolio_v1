from django.shortcuts import render, redirect
from .models import Experience, Project, Education
from .forms import ContactForm

# Create your views here.

def home(request):
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    return render(request, 'Mi_portafolio/home.html', {
        'projects': projects,
        'experiences': experiences,
        'educations': educations
    })


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success') 

    return redirect('home')

def contact_success(request):
    return render(request, 'Mi_portafolio/contact_success.html')
