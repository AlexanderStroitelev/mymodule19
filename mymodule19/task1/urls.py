from django.urls import path
from .views import PlatformView , GamesView , CartView
from . import views


app_name = 'task1'
urlpatterns = [
    path('platform/', PlatformView.as_view(), name='platform'),
    path('platform/games/', GamesView.as_view(), name='games'),
    path('platform/cart/', CartView.as_view(), name='cart'),
    path('django_sign_up', views.sign_up_by_django, name='sign_up_by_django'),
]
