from django.shortcuts import render
from django.http import HttpResponse
from .models import FormDetail
from .form import Detail_form
# Create your views here.


""" def form_Detail_view(request):
    form_obj = Detail_form(request.POST or None)
    if form_obj.is_valid():
        form_obj.save()
        form_obj = Detail_form()
    form_content = {
        "form_obj1" : form_obj
    }
    return render(request, "pages/form.html", form_content)    
 """

def form_Detail_view(request):
    if request.method == 'POST':
        NAME = request.POST.get('Name')
        AGE = request.POST.get('Age')
        ADDRESS = request.POST.get('Address')
        FormDetail.objects.create(Name=NAME, Age=AGE, Address=ADDRESS)
    print(request.POST)    
    form_content = {}    
    return render(request, "pages/form.html", form_content)


def homepage(Request,*arg, **kwargs):
    print(Request.user)
    #return HttpResponse("<h1>Hello World</h1>") 
    return render(Request, "home.html", {})

def contactpage(Request, *arg, **kwargs):
    contactme = {
        "developer" : "Aniket Singh",
        "Contact_No": 8929163145,
        "Email" : "ani.shiv.2018@gmail.com",
        "address": "1379-Govindpuri, New Delhi-110019",
    }
    return render(Request, "contact.html", contactme)

def aboutpage(Request, *arg, **kwargs):
    aboutme = {
        "developer" : "Aniket Singh",
        "Contact_No": 8929163145,
        "Email" : "ani.shiv.2018@gmail.com",
        "my_coures": ["Robotics", "NLP", "Block chain"],
    }
    return render(Request, "about.html", aboutme)        