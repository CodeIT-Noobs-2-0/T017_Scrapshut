from django.shortcuts import render, redirect
from donation.forms import DonationRegisterForm, DonatedByRegistrationForm
from donation.models import Donated, DonationItem
# Create your views here.

def register_donation(request):
    if request.method == 'POST':
        form = DonationRegisterForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_type = form.cleaned_data['item_type']
            quantity_required = form.cleaned_data['quantity_required']
            u = form.save(commit=False)
            user = form.save()
            user.save()
            return redirect('/')
    else:
        form = DonationRegisterForm()
    return render(request, 'donation_items.html', {'form': form})

def register_donated_by(request):
    if request.method == 'POST':
        form = DonatedByRegistrationForm(request.POST)
        if form.is_valid():
            donated_by = form.cleaned_data['donated_by']
            donated_item = form.cleaned_data['donated_item']
            donated_quantity = form.cleaned_data['donated_quantity']
            u = form.save(commit=False)
            user = form.save()
            user.save()
            return redirect('/')
    else:
        form = DonatedByRegistrationForm()
    return render(request, 'registered_donated_by.html', {'form': form})

def display_donation(request):
    items = DonationItem.objects.all
    args = {'items': items}
    return render(request, 'display_donation.html', args)

def display_donated_by(request):
    items = Donated.objects.all
    args = {'items': items}
    return render(request, 'display_donated_by.html', args)
