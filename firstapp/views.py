from django.shortcuts import render
from django.http import *
from .forms import UserForm


def index(request):
    wows = ["kek", "уии", "hehe"]
    langs = ["милый", "добрый", "весёлый"]
    data = {"header": "Hello Django!", "message": "Welcome to Python", "wows": wows, "spisok": langs}
    return render(request, "firstapp/index.html", context=data)


def user(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = request.POST.get("name")
            # также можно использовать name = userform.cleaned_data["name"]
            age = request.POST.get("age")
            return render(request, "firstapp/contacts.html", {"phone": "Добро пожаловать, {0}!".format(name)})
    return render(request, "firstapp/contacts.html", {"form": userform})


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "firstapp/about.html")


def contacts(request):
    return HttpResponse("<h2>Контакты</h2>")


def company_history(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=42):
    output = "<h3>Продукт №{}</h3>".format(productid)
    return HttpResponse(output)


def users(request, id=0, name="admin"):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)


def m404(request):
    return HttpResponseNotFound("<h5>404 Not Found</h5>")

# Create your views here.
