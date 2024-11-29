from django.shortcuts import render
from .models import Experience, Project, Education
from django.core.mail import send_mail
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                f"Mensaje de {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['tu_correo@gmail.com']
            )
            return render(request, 'Mi_portafolio/success.html')
    else:
        form = ContactForm()
    return render(request, 'Mi_portafolio/contact.html', {'form': form})