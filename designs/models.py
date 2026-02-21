from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Design(models.Model):
    CATEGORY_TYPE = [
        ('social','Social Media Ad'),
        ('card','Business Card'),
        ('flyer','Flyer/Poster'),
        ('rollup','Roll-up/Banner'),
        ('brand','Brand Identity'),
        ('other','Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='designs/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='designs')
    design_type = models.CharField(max_length=20, choices=CATEGORY_TYPE, default='other')  # optional helper
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
