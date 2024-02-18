from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'index.html', context)


def product_detail(request, product_id):
    context = {'product': Product.objects.get(id=product_id)}
    return render(request, 'index2.html', context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        # Обновляем поля товара с данными из формы
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')

        # Проверяем, было ли отправлено новое изображение
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()

        # После сохранения товара перенаправляем пользователя на страницу с деталями товара
        return redirect('product_detail', product_id=product_id)

    # Если запрос не методом POST, отображаем форму редактирования товара
    return render(request, 'edit.html', {'product': product})
