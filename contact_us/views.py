import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f"Contact Us Message from {name}",
                message=message,
                from_email=email,
                recipient_list=[os.environ.get('CONTACT_EMAIL')],
            )
            return redirect('contact_us_thanks')
    else:
        form = ContactForm()

    return render(request, 'contact_us/contact_us.html', {'form': form})

def thanks(request):
    return render(request, 'contact_us/thanks.html')