from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django import forms


# class NewForm(forms.Form):
#     user = forms.CharField(label='Пользователь')
#     password = forms.CharField(label='Пароль')
#     bb = forms.DecimalField(label='Дробь')
#     basket = forms.BooleanField(label="Пoлoжить товар в корзину")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        field = ('username', 'password')
