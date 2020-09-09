from django.shortcuts import render
from django.http import *
from .forms import UserForm
from .models import Person, Company, Product


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


def get_data(request):
    people = Person.objects.all()
    return render(request, "firstapp/test.html", {"people": people})


def create(request):
    if request.method == "POST":
        new_person = Person()
        new_person.name = request.POST.get("name")
        new_person.age = request.POST.get("age")
        new_person.save()
    return HttpResponseRedirect("/test")


def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/test")
        else:
            return render(request, "firstapp/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Такой не найден</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/test")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Как удалить того, кто и так не существует?..</h2>")


def goods_data(request):
    companies = Company.objects.all()
    goods = Product.objects.all()
    return render(request, 'firstapp/relationship.html', {"companies": companies, "goods": goods})


def create_company(request):
    if request.method == "POST":
        new_company = Company()
        new_company.name = request.POST.get("name")
        new_company.save()
    return HttpResponseRedirect("/relationship")


def edit_company(request, id):
    try:
        company = Company.objects.get(id=id)
        if request.method == "POST":
            company.name = request.POST.get("name")
            company.save()
            return HttpResponseRedirect("/relationship")
        else:
            return render(request, "firstapp/edit_company.html", {"company": company})
    except Company.DoesNotExist:
        return HttpResponseNotFound("<h2>Такой компании не существует.</h2>")


def delete_company(request, id):
    try:
        company = Company.objects.get(id=id)
        company.delete()
        return HttpResponseRedirect("/relationship")
    except Company.DoesNotExist:
        return HttpResponseNotFound("<h2>Такой компании не существует.</h2>")


def create_product(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        company_name = request.POST.get("company")
        company = Company.objects.get_or_create(name=company_name)
        company[0].product_set.add(product, bulk=False)
        product.save()
    return HttpResponseRedirect("/relationship")


# Create your views here.
