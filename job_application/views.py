from django.shortcuts import render
from .forms import ApplicationForm # . forms means import from current directory, otherise django will look at project app root directory-where forms is not available
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            ## FOR THE FOLLOWING CODES, NEED TO SET UP APP PASSWORD AND UPDATE SETTINGS.PY FILE AT THE BOTTOM. WILL DO LATER
            # message_body = f"A new job application was submitted. Thank you. {first_name}"
            # email_message = EmailMessage("form submission confirmation", message_body, to=[email])
            # email_message.send()

            messages.success(request,"Form submitted successfully!")

    return render(request,"index.html")
