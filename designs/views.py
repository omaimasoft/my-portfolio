from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator  # ✅ ضروري
from .models import Design, Category


def designs_list(request):
    cat_slug = request.GET.get("category")
    categories = Category.objects.all()

    designs_qs = Design.objects.filter(published=True).select_related("category").order_by("-id")
    if cat_slug:
        designs_qs = designs_qs.filter(category__slug=cat_slug)

    paginator = Paginator(designs_qs, 16)  # ✅ 10 فكل صفحة (بدّليها)
    page_number = request.GET.get("page")
    designs = paginator.get_page(page_number)

    return render(request, "designs/designs_list.html", {
        "designs": designs,
        "categories": categories,
        "active_slug": cat_slug,
    })


def design_detail(request, pk):
    design = get_object_or_404(Design, pk=pk, published=True)
    return render(request, "designs/design_detail.html", {"design": design})