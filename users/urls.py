from django.urls import path, re_path
from .views import login, registration, test, products, users

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registrations/', registration, name='registration'),
    re_path(r'^tes?', test, name='test'),
#    path('products/', products),
    path('products/<int:productid>/', products),
    path('users/', users),
#    path('users/<int:nameid>/<str:name>', users),

]