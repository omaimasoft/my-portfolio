# projects/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import Project, Service, Profile, SocialLink, Skill
from designs.models import Design
from printed.models import PrintedProduct
from .forms import ContactForm

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})
# skills/views.py

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {'skills': skills})
# services/views.py

def service_list(request):
    services = Service.objects.all()
    return render(request, "services/service_list.html", {"services": services})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("projects:contact")
    else:
        form = ContactForm()
    return render(request, "projects/contact.html", {"form": form})
# servise 


def services(request):
    services = Service.objects.all()
    return render(request, "projects/services.html", {"services": services})
# progict
from django.shortcuts import render
from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})

# skilsse


def skills(request):
    skills = Skill.objects.all()
    return render(request, "projects/skills.html", {"skills": skills})



def home(request):
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()

    latest_projects = Project.objects.all().order_by('-created_at')[:3]
    latest_designs = Design.objects.all().order_by('-id')[:3]
    services = Service.objects.all()[:3]
    top_skills = Skill.objects.all()[:5]
    products = PrintedProduct.objects.all()[:4]   # ✅ عرض 6 منتجات

    context = {
        "profile": profile,
        "social_links": social_links,
        "projects": latest_projects,
        "designs": latest_designs,
        "services": services,
        "top_skills": top_skills,
        "products": products,   # ✅ مهم جداً
    }

    return render(request, "projects/home.html", context)

# views.py

def skills_json(request):
    skills = list(Skill.objects.values())
    return JsonResponse(skills, safe=False)
