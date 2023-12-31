from django.http import *
from django.shortcuts import render

from users.forms import UserForm
from users.forms import UserLoginForm
from users.models import User


# Create your views here.
def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт No {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    nameid = request.GET.get("id", 1)
    name = request.GET.get('name', 'Макс')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(nameid, name)
    return HttpResponse(output)


def forms_lable(request):
     userform = UserForm()
     if request.method == 'POST':
         userform = UserForm(request.POST)
         if userform.is_valid():
             name =userform.cleaned_data["name"]
             return HttpResponse(f'Имя введено корректно {name}')

         # else:
         #     return HttpResponse(f'Ошибка')

     return render(request, 'users/test.html', {'form': userform})


# def test(request):
#     content = {'form': UserLoginForm}
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         output = f"<h2>Пользователь</h2><h3>Имя - {name}</h3> <h3>Возраст - {age}</h3>"
#
#         return HttpResponse(output)
#     else:
#         userform = UserForm()
#         return render(request, 'users/test.html', {'form': userform})