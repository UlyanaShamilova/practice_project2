from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

# Create your views here.
def auth(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
            else:
                context['error'] = 'Логін або пароль невірні'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, 'authrization_registration/auth.html', context)

def reg(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        context["login"] = login
        context["name"] = name
        context["surname"] = surname
        context["password"] = password
        context["confirm_password"] = confirm_password

        if login and name and surname and password and confirm_password:
            if len(password) >= 8:
                if password == confirm_password:
                    try:
                        User.objects.create_user(
                            username=login, 
                            password=password,
                            first_name=name, 
                            last_name=surname
                            )
                        return redirect('auth')
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
                else:
                    context["error"] = "Паролі не співпадають"
            else:
                context["error"] = "Пароль не менше ніж 8 символів!"  
        else:
            context["error"] = "Заповніть всі поля!"



    return render(request, 'authrization_registration/registration.html', context)