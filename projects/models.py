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


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0, help_text="من 0 إلى 100")
    image = models.ImageField(upload_to="skills/", blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"رسالة من {self.name}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Omaima Boustik")
    role = models.CharField(max_length=100, default="Fullstack Developer")
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)

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
        ("codepen", "Codepen"),
    ]

    name = models.CharField(max_length=50)
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