from django.contrib import admin
from .models import Book
from . models import GuitarAkk
from . models import GuitarEl
from . models import Equipments
from . models import Key

# Register your models here.

admin.site.register(Book)
admin.site.register(GuitarAkk)
admin.site.register(GuitarEl)
admin.site.register(Equipments)
admin.site.register(Key)