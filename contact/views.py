from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if email:
            try:
                send_mail(
                    subject,
                    f'Nombre: {name}\nCorreo Electrónico: {email}\nMensaje: {message}',
                    email,
                    ['bibliotia1@gmail.com'],  
                    fail_silently=False,
                )

                return HttpResponseRedirect(reverse('contact:contact'))
            except BadHeaderError:
                messages.error(request, 'Credenciales invalidas', extra_tags='danger')
                return redirect('contact:contact')
        else:
            messages.error(request, 'Credenciales invalidas', extra_tags='danger')
            return redirect('contact:contact')
    
    return render(request, 'contact/contact.html')

def phone(request):
    return render(request, 'contact/phone.html')