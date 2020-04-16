from django.urls import reverse
from django.shortcuts import render, resolve_url
from .models import Item, Contact
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
from .forms import ContactForm


class ContactCreateView(CreateView):
    template_name = 'contact_create.html'
    form_class = ContactForm
    # queryset = Contact.objects.all()

    def get_success_url(self):
        return resolve_url('../home/')


class ContactListView(ListView):
    template_name = 'home-page.html'
    queryset = Item.objects.all()

    # def home_page(request):
    #     context = {
    #         'items': Item.objects.all()
    #     }
    #     return render(request, 'home-page.html', context)

    # def contact_page(request):
    #     context = {
    #         'items': Item.objects.all()
    #     }
    #     return render(request, 'contact.html', context)

    # def category_page(request):
    #     context = {
    #         'items': Item.objects.all()
    #     }
    #     return render(request, 'category-page.html', context)

    # def post_page(request):
    #     context = {
    #         'items': Item.objects.all()
    #     }
    #     return render(request, 'post-page.html', context)
