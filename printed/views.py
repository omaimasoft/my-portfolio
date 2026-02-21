from django.shortcuts import render, get_object_or_404
from .models import PrintedProduct, PrintedCategory


def printed_list(request):
    products = PrintedProduct.objects.select_related("category")
    categories = PrintedCategory.objects.all()

    return render(request, "printed/printed_list.html", {
        "products": products,
        "categories": categories,
    })


def printed_detail(request, slug):
    product = get_object_or_404(PrintedProduct, slug=slug)

    return render(request, "printed/printed_detail.html", {
        "product": product
    })
