# projects/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/images/")
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# skills/models.py
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0, help_text="من 0 إلى 100")
    image = models.ImageField(upload_to='skills/', blank=True, null=True)  # لحفظ صورة المهارة

    def __str__(self):
        return self.name

# pages/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"رسالة من {self.name}"


# services/models.py
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title
# PORTFOLYO
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Omauma Boustik")
    role = models.CharField(max_length=100, default="Fullstack Developer")
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="profiles/")  # هادي الصورة الشخصية

    def __str__(self):
        return self.name

# LES CONTACTE
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profiles/")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    ICON_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("whatsapp", "WhatsApp"),
        ("twitter", "Twitter"),
        ("github", "GitHub"),
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("envelope", "Email"),
        ("codepen", "Codepen"), # يستعمل bxl-codepen
    ]

    name = models.CharField(max_length=50)  # مثلا: "حساب لينكدإن"
    url = models.URLField()
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default="linkedin"
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="social_links"
    )

    def __str__(self):
        return f"{self.name} ({self.icon})"
