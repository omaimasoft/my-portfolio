# projects/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.cache import cache

from .models import Project, Service, Profile, SocialLink, Skill
from designs.models import Design
from printed.models import PrintedProduct
from .forms import ContactForm


# ======================================================
# GET CLIENT IP
# نحصل على IP ديال الزائر لمنع السبام
# ======================================================

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


# ======================================================
# HOME PAGE
# الصفحة الرئيسية
# ======================================================

def home(request):
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()

    # ✅ المشاريع التي تختارينها من Admin للصفحة الرئيسية
    latest_projects = Project.objects.filter(
        show_on_homepage=True
    ).order_by("homepage_order", "-created_at")[:3]

    # ✅ إذا لم تختاري أي مشروع، يعرض آخر 3 مشاريع تلقائياً
    if not latest_projects.exists():
        latest_projects = Project.objects.all().order_by("-created_at")[:3]

    latest_designs = Design.objects.all().order_by("-id")[:3]
    services = Service.objects.all()[:3]
    top_skills = Skill.objects.all()[:5]
    products = PrintedProduct.objects.all()[:4]

    context = {
        "profile": profile,
        "social_links": social_links,
        "projects": latest_projects,
        "designs": latest_designs,
        "services": services,
        "top_skills": top_skills,
        "products": products,
    }

    return render(request, "projects/home.html", context)
# ======================================================
# CONTACT PAGE
# صفحة التواصل مع حماية ضد السبام
# ======================================================

def contact(request):
    social_links = SocialLink.objects.all()

    if request.method == "POST":
        ip = get_client_ip(request)
        cache_key = f"contact_form_limit_{ip}"

        # منع نفس الزائر من إرسال رسالة أخرى خلال 60 ثانية
        if cache.get(cache_key):
            messages.error(
                request,
                "Please wait a little before sending another message."
            )
            return redirect("projects:contact")

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # قفل الإرسال لمدة 60 ثانية لهذا IP
            cache.set(cache_key, True, 60)

            messages.success(
                request,
                "Your message has been sent successfully!"
            )
            return redirect("projects:contact")

        messages.error(
            request,
            "Your message could not be sent. Please check the form."
        )

    else:
        form = ContactForm()

    context = {
        "form": form,
        "social_links": social_links,
    }

    return render(request, "projects/contact.html", context)


# ======================================================
# PROJECT LIST PAGE
# صفحة قائمة المشاريع
# ======================================================

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")

    return render(request, "projects/project_list.html", {
        "projects": projects
    })


# ======================================================
# PROJECTS PAGE
# صفحة المشاريع
# ======================================================

def projects(request):
    projects = Project.objects.all().order_by("-created_at")

    return render(request, "projects/projects.html", {
        "projects": projects
    })


# ======================================================
# SERVICES PAGE
# صفحة الخدمات
# ======================================================

def services(request):
    services = Service.objects.all()

    return render(request, "projects/services.html", {
        "services": services
    })


# ======================================================
# SERVICE LIST PAGE
# صفحة قائمة الخدمات إذا كنت تستعملينها
# ======================================================

def service_list(request):
    services = Service.objects.all()

    return render(request, "services/service_list.html", {
        "services": services
    })


# ======================================================
# SKILLS PAGE
# صفحة المهارات
# ======================================================

def skills(request):
    skills = Skill.objects.all()

    return render(request, "projects/skills.html", {
        "skills": skills
    })


# ======================================================
# SKILL LIST PAGE
# صفحة قائمة المهارات إذا كنت تستعملينها
# ======================================================

def skill_list(request):
    skills = Skill.objects.all()

    return render(request, "skills/skill_list.html", {
        "skills": skills
    })


# ======================================================
# SKILLS JSON
# API بسيط للمهارات
# ======================================================

def skills_json(request):
    skills = list(Skill.objects.values())

    return JsonResponse(skills, safe=False)