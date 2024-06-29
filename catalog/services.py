from catalog.models import Product, ProductCategory
from config.settings import CACHE_ENABLED
from django.core.cache import cache
from catalog.models import ProductCategory


def get_products_from_cache():
    """
    получает список продуктов из кеша
    иначе возвращает список продуктов из БД и сохраняет их в кеш.
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_categories_from_cache():
    """
    Получает список категорий из кеша,
    иначе возвращает список категорий из БД и сохраняет их в кеш.
    """
    if not CACHE_ENABLED:
        return ProductCategory.objects.all()

    key = 'category_list'
    categories = cache.get(key)
    if categories is not None:
        return categories

    categories = ProductCategory.objects.all()
    cache.set(key, categories)
    return categories
