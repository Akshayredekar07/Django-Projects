from django.shortcuts import render
from durga.models import Company
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class CompanyListView(ListView):
    model=Company
    # company_list.html && company_list 

# durga/views.py
from django.views.generic import DetailView
from durga.models import Company

class CompanyDetailView(DetailView):
    model = Company
    template_name = "durga/company_detail.html"  # Ensure this is correct


class CompanyCreateView(CreateView):
    model=Company
    #fields: ('name', 'location', 'ceo')
    fields='__all__'   
    # default template fiename: company_form.html


class CompanyUpdateView(UpdateView):
    model=Company
    fields=('location', 'ceo')
    # default template file: company_form.htlm
    #     


class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('list')
