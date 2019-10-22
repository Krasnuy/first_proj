from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.conf import settings

# end email confirm register -- чуть импортов и все пошло-поехало ;)
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookForm


def login_(request):
    ctx = {}
    if request.method == 'GET':
        return render(request, "client_app/login_form.html", ctx)
    elif request.method == 'POST':
        username = request.POST.get('username1')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            ctx['error'] = 'Неверный логин или пароль или ты не активный))) .'
            return render(request, "client_app/login_form.html", ctx)


def logout_(request):
    logout(request)
    return redirect('/')


def register_(request):
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = SignUpForm()
        return render(request, 'client_app/register_form.html', ctx)
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        check_mail = bool(request.POST.get('check_mail'))
        print(check_mail)
        if form.is_valid():
            user = form.save(check_mail=check_mail)
            current_site = get_current_site(request)
            message = render_to_string('mail/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            if check_mail:
                mail_subject = 'Пітвердження пошти для реєстрації.'
                to_email = form.get_cleaned_data()['email']
                email = EmailMessage(mail_subject, message, to=[to_email , ''])
                email.send()
                return HttpResponse('Зайдіть будь ласка на вашу почту для продовження реєстрації.')
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)

            return redirect('/')

        else:
            ctx['form'] = SignUpForm(request.POST)
    return render(request, 'client_app/register_form.html', ctx)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
    ctx = {
        'confirmation_ok': True
    }
    return render(request, 'client_app/login_form.html', ctx)
