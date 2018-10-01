from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ayomi3 import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.template.loader import render_to_string


def Login(request):
    next = request.GET.get('next', '/profile/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "app/login.html", {'redirect_to': next})


def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


@login_required
def Home(request):
    return render(request, "app/home.html", {})

@login_required
def profile(request):
    context={'user': request.user}
    return render(request, "app/profile.html", context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            user = request.user
            data['profile'] = render_to_string('app/profile1.html', {'user': user})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
    else:
        form = UserForm(instance=user)
    return save_all(request, form, 'app/editprofile.html')
