"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('contacts/', TemplateView.as_view(template_name="firstapp/contacts.html",
                                           extra_context={"phone": "8 800 555 35 35"})),
    path('', views.index, name="home"),
    path('users/', views.users),
    path('users/<int:id>/<name>/', views.users),
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    path('company/', views.company_history),
    path('details/', views.details),
    path('home/', views.home),
    path('user/', views.user),
    path('test/', views.get_data),
    path('test/create/', views.create),
    path('test/edit/<int:id>/', views.edit),
    path('test/delete/<int:id>/', views.delete),
    path('relationship/', views.goods_data),
    path('relationship/create_company/', views.create_company),
]
