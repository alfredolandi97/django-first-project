from django.urls import path
from first_app import views

#TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.form_name_view, name='forms'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('registration/', views.register, name='registration'),
    path('user_login/', views.user_login, name="user_login")
]
