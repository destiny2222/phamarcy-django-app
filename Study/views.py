from django.shortcuts import render,redirect
from .forms import FeedbackForm
from django.contrib import messages
from django.core.mail import mail_admins,send_mail

# Create your views here.


def tutorView(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['course']
            subject = "You have a new Feedback to Tutor me from {}:{}".format(name, sender) 
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['course'], f.cleaned_data['note'])
            mail_admins(subject, message, fail_silently=False)
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('index:tutor')
    else:
        f = FeedbackForm()
    return render(request, 'account/tutor.html', {'form': f})