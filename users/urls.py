from django.urls import path, re_path


from .views import forms_lable, registration, products, users, login #test

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registrations/', registration, name='registration'),
    path('t', forms_lable),
    #re_path(r'^tes?', test, name='test'),
    path('products/', products),
    path('products/<int:productid>/', products),
    path('', users),


#    path('users/<int:nameid>/<str:name>', users),

]