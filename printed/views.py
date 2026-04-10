from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import PrintedProduct, PrintedCategory


def printed_list(request):
    products_qs = PrintedProduct.objects.select_related("category").all().order_by("-id")
    categories = PrintedCategory.objects.all()

    paginator = Paginator(products_qs, 16)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "printed/printed_list.html", {
        "products": products,
        "categories": categories,
        "page_obj": products,
    })


def printed_detail(request, slug):
    product = get_object_or_404(
        PrintedProduct.objects.select_related("category"),
        slug=slug
    )

    # منتجات مشابهة من نفس التصنيف
    related_products = PrintedProduct.objects.filter(
        category=product.category
    ).exclude(id=product.id).order_by("-id")[:4]

    # مؤقتًا: آخر المنتجات
    # إلى كان عندك sold_count بدليه بـ order_by("-sold_count")
    best_sellers = PrintedProduct.objects.exclude(
        id=product.id
    ).order_by("-id")[:4]

    return render(request, "printed/printed_detail.html", {
        "product": product,
        "related_products": related_products,
        "best_sellers": best_sellers,
    })