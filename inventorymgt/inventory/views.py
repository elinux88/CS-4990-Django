from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Item, Category

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = model_to_dict(self.object)
            return JsonResponse(data)
        else:
            return response

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class CreateCategoryView(CreateView):
    model = Category
    fields = ['parent', 'name', 'description']

    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.pk,))

class UpdateCategoryView(UpdateView):
    model = Category
    fields = ['parent', 'name', 'description']

    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.pk,))

class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('inventory:categorydeletesuccess')

class ItemListView(ListView):
    model = Item

class ItemDetailView(DetailView):
    model = Item

    def render_to_response(self, context, **kwargs):
        if self.request.is_ajax():
            return JsonResponse(searializers.serialize('json', self.object))
        return super(ItemDetailView, self).render_to_response(context, **kwargs)

class CreateItemView(CreateView):
    model = Item
    fields = ['name', 'quantity', 'sku', 'category']
    success_url = reverse_lazy('inventory:additem')

class UpdateItemView(AjaxableResponseMixin, UpdateView):
    model = Item
    fields = ['category', 'name', 'sku', 'quantity']
    success_url = reverse_lazy('inventory:updateitem')

#   def get_context_data(self, *args, **kwargs):
#       context = super(UpdateItemView, self).get_context_data(**kwargs)
#       context["item_form"] = ItemForm(initial={'quantity': 0})
#       return context

class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy('inventory:itemdeletesuccess')

