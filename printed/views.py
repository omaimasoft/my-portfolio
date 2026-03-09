from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator  # ✅ مهم
from .models import PrintedProduct, PrintedCategory


def printed_list(request):
    products_qs = PrintedProduct.objects.select_related("category").all().order_by("-id")
    categories = PrintedCategory.objects.all()

    paginator = Paginator(products_qs, 18)  # ✅ هنا العدد اللي بغيتي (10)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "printed/printed_list.html", {
        "products": products,
        "categories": categories,
        "page_obj": products,
    })


def printed_detail(request, slug):
    product = get_object_or_404(PrintedProduct, slug=slug)
    return render(request, "printed/printed_detail.html", {"product": product})