from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages



# Create your views here.


def contact(request):
    form_class = Contact

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get(  
                'name'
            , '')
            email = request.POST.get(
                'email'
            , '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')


            # Email the profile with the
            # contact information
           
            context = {
                'name': name,
                'contact_email': email,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['linalukusa@gmail.com'],
                headers = {'Reply-To': email }
            )
            email.send()
            return redirect('Contact/contact')

    return render(request, 'Contact/contact.html', {
        'form': form_class,
    })
