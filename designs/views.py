from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, Category

def designs_list(request):
    cat_slug = request.GET.get('category')
    categories = Category.objects.all()
    if cat_slug:
        designs = Design.objects.filter(category__slug=cat_slug, published=True)
    else:
        designs = Design.objects.filter(published=True)
    return render(request, 'designs/designs_list.html', {
        'designs': designs,
        'categories': categories,
        'active_slug': cat_slug,
    })

def design_detail(request, pk):
    design = get_object_or_404(Design, pk=pk, published=True)
    return render(request, 'designs/design_detail.html', {'design': design})
