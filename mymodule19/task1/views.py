from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import Buyer
from .models import Game


class PlatformView(TemplateView):
    template_name = 'fourth_task/platform.html'

class GamesView(TemplateView):
    template_name = 'fourth_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = Game.objects.all()
        context['games'] = games
        context['purchase_link'] = 'Купить'
        return context

class CartView(TemplateView):
    template_name = 'fourth_task/cart.html'


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                info['message'] = f'Приветствуем, {username}!'

        info['form'] = form
    else:
        info['form'] = UserRegister()

    return render(request,'fifth_task/registration_page.html', info)
