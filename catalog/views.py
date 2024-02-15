from django.shortcuts import render

from catalog.models import Product


# Create your views here
def index(request):
    context = {'products': Product.objects.all()}
    # for product in context['products']:
    #     if len(product.description) > 100:
    #         product.description = product.description[:97] + '...'
    #     if len(product.name) > 16:
    #         product.name = product.name[:13] + '...'
    return render(request, 'index.html', context)
