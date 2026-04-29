from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# ===================== CATEGORY =====================

class PrintedCategory(models.Model):
    name = models.CharField("Category Name", max_length=100)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        verbose_name = "Printed Category"
        verbose_name_plural = "Printed Categories"

    def __str__(self):
        return self.name


# ===================== PRODUCT =====================

class PrintedProduct(models.Model):
    category = models.ForeignKey(
        PrintedCategory,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Category"
    )

    title = models.CharField("Product Title", max_length=150)

    slug = models.SlugField(
        "Slug",
        unique=True,
        blank=True
    )

    main_image = models.ImageField(
        "Main Image",
        upload_to="printed/main/"
    )

    description = models.TextField(
        "Product Description",
        blank=True
    )

    short_description = models.TextField(
        "Short Description",
        blank=True
    )

    price = models.DecimalField(
        "Price (MAD)",
        max_digits=8,
        decimal_places=2
    )

    capacity = models.CharField(
        "Capacity",
        max_length=50,
        blank=True
    )

    material = models.CharField(
        "Material",
        max_length=100,
        blank=True
    )

    lid = models.CharField(
        "Lid",
        max_length=100,
        blank=True
    )

    straw = models.CharField(
        "Straw",
        max_length=100,
        blank=True
    )

    design = models.CharField(
        "Design",
        max_length=150,
        blank=True
    )

    use = models.CharField(
        "Use",
        max_length=150,
        blank=True
    )

    care = models.CharField(
        "Care Instructions",
        max_length=150,
        blank=True
    )

    is_available = models.BooleanField(
        "In Stock",
        default=True
    )

    delivery_info = models.CharField(
        "Delivery Info",
        max_length=150,
        blank=True,
        default="Delivery available in Morocco"
    )

    video = models.FileField(
        "Product Video (Optional)",
        upload_to="printed/videos/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        "Featured Product",
        default=False
    )

    created_at = models.DateTimeField(
        "Created At",
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Printed Product"
        verbose_name_plural = "Printed Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            i = 1

            while PrintedProduct.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{i}"
                i += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("printed:detail", args=[self.slug])

    def __str__(self):
        return self.title


# ===================== GALLERY =====================

class PrintedProductImage(models.Model):
    product = models.ForeignKey(
        "PrintedProduct",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Product"
    )

    image = models.ImageField(
        "Additional Image",
        upload_to="printed/gallery/"
    )

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"Image - {self.product.title}"