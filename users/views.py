from django.http import HttpResponse
from django.shortcuts import render
from users.forms import UserLoginForm
from users.models import User


# Create your views here.
def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')


def test(request):
    content = {'form': UserLoginForm}
    return render(request, 'users/test.html', content)


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт No {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    nameid = request.GET.get("id", 1)
    name = request.GET.get('name', 'Макс')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(nameid, name)
    return HttpResponse(output)
