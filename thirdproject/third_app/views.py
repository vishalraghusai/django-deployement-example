from django.shortcuts import render
from third_app import form
# Create your views here.
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    registered = False
    user_form = form.Userinfoform()
    profile_form = form.userinfoform()

    if request.method == 'POST':
        user_form = form.Userinfoform(data = request.POST)
        profile_form = form.userinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pics' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered= True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = form.Userinfoform()
        profile_form = form.userinfoform()



    return render(request, 'register.html',{'user_form':user_form,
                                            'profile_form':profile_form,
                                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            print('someone tried to login nd failed')
            print('Username :{} and password: {}'.format(username,password))
            return HttpResponse('invalid passwod or username') and render(request,'login.html')
    else:
        return render(request, 'login.html',{})
@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


