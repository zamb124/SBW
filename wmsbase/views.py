from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse

@login_required(login_url='login/')
def index(request):
    path = {'path': request.path}

    return render(request,'index.html', path)
# Create your views here.



def login(request): # Вход в приложение
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active: # Проверяем юзера на активность
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)# логинимся в систему
            try:
                next = request.GET['next']
                return HttpResponseRedirect(next)
            except:
                # Перенаправление на "правильную" страницу
                return HttpResponseRedirect('/')
        else:
            # Отображение страницы с ошибкой
            return render(request, 'page-login.html', {'usererror': username})
    else:
        return render(request, 'page-login.html')

@login_required(login_url='/login/')
def logout(request): #
    auth.logout(request)
    return HttpResponseRedirect('/login/')