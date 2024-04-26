from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import Group#, User
from django.contrib.auth import authenticate, login, logout 
#from schedule_app.decorators import allowed_users
from ..forms import LoginForm, CreateUserForm

def registerPage(request):
    form = CreateUserForm()
    cleaner_group = Group.objects.get(name='cleaner_role')

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user.groups.add(cleaner_group)
            messages.success(request, f'Account created for {username}')
            #auth_user = User(username=username, password=password)
            print(f'Created user: {user}')
            return redirect('login')

    context = {'form':form}
    return render(request, 'schedule_app/registration/register.html', context)

def loginPage(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print(f'user: {user}\nlogged in')
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {'form':form}
    return render(request, 'schedule_app/registration/login.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('index')