from django.shortcuts import render
from django.http import *
from .forms import UserForm
from .models import Person


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


def test_models(request):
    """
    CRUD
    create
    """
    tom = Person.objects.create(name="Tom", age=23)
    jennifer = Person(name="Jennifer", age=23)
    jennifer.save()
    timmy = Person.objects.create(name="Timmy", age=18)
    #wow = Person.objects.get_or_create(name="Timmy")
    people = Person.objects.all()
    people_list = []
    for person in people:
        people_list.append(person.name)
    peeeople = Person.objects.filter(name="Tom").exclude(age=34)
    return HttpResponse(f"<h2>{tom.id}, {jennifer.age}, {jennifer.name}<br><br>{people_list}</h2><br>{peeeople.query}")


def m404(request):
    return HttpResponseNotFound("<h5>404 Not Found</h5>")

# Create your views here.
