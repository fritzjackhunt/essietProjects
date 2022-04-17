from django.views.generic.edit import CreateView
from .models import Newsletter
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from .forms import NewsletterForm
from django.views.generic import FormView, View

def home(request):
    return render(request, 'zloggr/index.html')

def home1(request):
    return render(request, 'zloggr/index1.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['info.zloggr@gmail.com'],
            fail_silently = False,
        )


        return render(request, 'zloggr/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'zloggr/contact.html')


class NewsletterView(CreateView):
    model = Newsletter
    template_name = 'zloggr/about.html'
    form_class = NewsletterForm
    success_url = 'success'


def success(request):
    return render(request, 'zloggr/success.html')

def huawei(request):
    return render(request, 'zloggr/huawei.html')

def amazon(request):
    return render(request, 'zloggr/amazon.html')

def sony(request):
    return render(request, 'zloggr/sony.html')

def blog1(request):
    return render(request, 'zloggr/blog1.html')

def blog2(request):
    return render(request, 'zloggr/blog2.html')

def blog3(request):
    return render(request, 'zloggr/blog3.html')

def blog4(request):
    return render(request, 'zloggr/blog4.html')

def blog5(request):
    return render(request, 'zloggr/blog5.html')

def blog6(request):
    return render(request, 'zloggr/blog6.html')

def blog7(request):
    return render(request, 'zloggr/blog7.html')

def blog8(request):
    return render(request, 'zloggr/blog8.html')

def blog9(request):
    return render(request, 'zloggr/blog9.html')

def internetvpn(request):
    return render(request, 'zloggr/internetvpn.html')

def blackfridaydeal(request):
    return render(request, 'zloggr/blackfridaydeal.html')

def expressvpn(request):
    return render(request, 'zloggr/expressvpn.html')

def security(request):
    return render(request, 'zloggr/security.html')

