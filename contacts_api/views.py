from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Company
from .forms import CompanyForm

# Create your views here.
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ContactSerializer # tell django what serializer to use

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer

# View to list all companies
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'contacts_api/company_list.html', {'companies': companies})

# View to add a new company
def company_add(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('company_list'))
    else:
        form = CompanyForm()
    return render(request, 'contacts_api/company_form.html', {'form': form})

# View to update an existing company
def company_edit(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('company_list'))
    else:
        form = CompanyForm(instance=company)
    return render(request, 'contacts_api/company_form.html', {'form': form})

# View to delete a company
def company_delete(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        company.delete()
        return HttpResponseRedirect(reverse('company_list'))
    return render(request, 'contacts_api/company_confirm_delete.html', {'company': company})