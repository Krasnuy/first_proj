from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import GuitarAkk
from .models import GuitarEl
from .models import Equipments
from .models import Key


# Create your views here.
def index(request):
    ctx = {}
    ctx['a'] = 45
    all_books = Book.objects.all()
    ctx['all_books'] = all_books
    for book in all_books:
        print(book.title)
    # print(all_books)
    return render(request, 'index.html', ctx)


def about(request):
    return render(request, 'about.html', {})


def input(request):
    return render(request, 'input.html', {})


def guitar(request):
    ctx = {}
    all_guitar = GuitarAkk.objects.all()
    ctx['all_guitar'] = all_guitar
    for guitarakk in all_guitar:
        print(guitarakk.title)
    return render(request, 'guitar.html', ctx)


def elguitar(request):
    ctx = {}
    all_elguitar = GuitarEl.objects.all()
    ctx['all_elguitar'] = all_elguitar
    for elguitar in all_elguitar:
        print(elguitar.title)
    return render(request, 'elguitar.html', ctx)


def cabinet(request):
    ctx = {}
    return render (request, 'private_cab.html', ctx)


def equipments(request):
    ctx = {}
    all_equip = Equipments.objects.all()
    ctx['all_equip'] = all_equip
    for equip in all_equip:
        print(equip.title)
    return render(request, 'equipments.html', ctx)

def keys(request):
    ctx = {}
    all_key = Key.objects.all()
    ctx['all_key'] = all_key
    for key in all_key:
        print(key.title)
    return render(request, 'key.html', ctx)



def actions(request):
    ctx = {}
    return render(request, 'actions.html', ctx)


def contacts(request):
    ctx = {}
    return render(request, 'contacts.html', ctx)



