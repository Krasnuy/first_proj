from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app1.models import Book
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Author
from .forms import AuthorForm



# Create your views here.

@login_required(redirect_field_name=settings.LOGIN_URL)
def cabinet(request):
    ctx = {}
    ctx['cabinet_tab'] = 'main'
    if request.method == 'GET':
        try:
            author = Author.objects.get(user=request.user.id)
            ctx['form'] = AuthorForm(instance=author)
        except Exception as e:
            ctx['form'] = AuthorForm
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user.id)
            author.date_birth = form.cleaned_data['date_birth']
            author.bio = form.cleaned_data['bio']
            author.type_view = form.cleaned_data['type_view']
            author.pseudoname = form.cleaned_data['pseudoname']
            author.save()
            ctx['save'] = True
            ctx['form'] = AuthorForm(instance=author)
        else:
            ctx['form'] = AuthorForm(request.POST)
    return render(request, 'client_app/cabinet.html', ctx)


def index(request):
    all_books = Book.objects.all()  # 'SELECT * FROM wa_1_book;'
    return render(request, 'pages/home.html', {
        'a': 'Hello django!',
        'all_books': all_books,
    })


def about(request):
    return render(request, 'pages/about.html', {})


def book_info(request, pk):
    ctx = {}
    ctx['book'] = Book.objects.get(pk=pk)
    return render(request, 'pages/book_info.html', ctx)


import datetime


def filter_by_category(request, pk):
    all_books_in_category = Book.objects.filter(category__id=pk)
    return render(request, 'pages/home.html', {

        'all_books': all_books_in_category,
    })


def filters(request):
    ctx = {}
    ctx['some_text'] = 'lORem ipSum'
    ctx['var'] = 'rrrrrr'
    ctx['number'] = 5
    ctx['first_list'] = range(40)
    ctx['second_list'] = Book.objects.all()
    ctx['x'] = 1
    # if var == 'a':
    #     pass
    # elif var == 'b':
    #     pass
    # else:
    #     pass
    people = [
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
    ]
    ctx['people'] = people
    ctx['date'] = datetime.datetime.now()
    return render(request, 'partials/filters.html', ctx)


def html_example(request):
    # from .calc import calc_obj
    # ctx = {
    #     'operations': calc_obj.keys()
    # }
    # if request.GET.get('hidden_value'):
    #     try:
    #         first = float(request.GET.get('first_number'))
    #         second = float(request.GET.get('second_number'))
    #         oper = request.GET.get('oper')
    #         result = calc_obj[oper](first, second)
    #         ctx['result'] = result
    #         ctx['first'] = first
    #         ctx['second'] = second
    #     except (ZeroDivisionError, ValueError) as e:
    #         ctx['error'] = e
    return render(request, 'partials/html_example.html', {})


def return_json(request):
    return JsonResponse({
        'status': True,
        'data': {
            'id': 1,
            'name_user': 'admin',
            'password': 'qwerty'
        }
    })


# from .calc import calc_obj


def calculator(request):
    # ctx = {}
    # ctx['operations'] = calc_obj.keys()
    # print(calc_obj.keys())
    return render(request, 'client_app/calculator.html', {})


from .forms import DemoForm


def demo_model_form(request):
    ctx = {}
    form = DemoForm()
    ctx['demo_form'] = form
    if request.method == 'GET':
        ctx['demo_form'] = form
    elif request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['name'])
        # print(form.is_valid())
        # print(form)
        print('POOOOST!!!!')
    # print(form)
    return render(request, 'pages/demo_model_form.html', ctx)


# import requests


# def api_privatbank(request):
#     data_from_api = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
#     print(request.META)
#     return render(request, 'pages/privatbank.html', {
#         'data': data_from_api.json()
#     })
