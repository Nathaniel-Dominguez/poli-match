from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('politicians', views.politicians, name='politicians'),
    path('politicians/<int:pk>', views.politician_detail, name='politician_detail'),
    path('quotes', views.quotes, name='quotes'),
]