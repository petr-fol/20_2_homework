from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, ProductVersion
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from catalog.services import get_products_from_cache


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    # permission_required = 'catalog.view_product'

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    # permission_required = 'catalog.view_product'


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    # permission_required = 'catalog.add_product'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'slug': self.object.slug})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # permission_required = 'catalog.change_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, ProductVersion, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = SubjectFormset(self.request.POST, instance=self.object)
        else:
            formset = SubjectFormset(instance=self.object)
        context_data['formset'] = formset
        context_data['is_editing'] = True
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit_category") and \
                user.has_perm("catalog.can_edit_is_published") and \
                user.has_perm("catalog.can_edit_description"):
            return ProductModeratorForm
        raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'slug': self.object.slug})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    # permission_required = 'catalog.delete_product'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
