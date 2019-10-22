from django import template
# from app1.models import Category
# import requests

register = template.Library()


@register.filter
def capitalize_custom(str_):
    # list_ = str_.split()
    # for elem in list_:
    #     tmp = elem.split()
    #     print(tmp)
    #     tmp[0][0].upper()
    #     # x = tmp[0][0].upper()
    #     # print(x)
    #     # tmp[0][0] = x
    #     result_str = ''.join([char for char in tmp])
    #     print(result_str)
    # # list_ = [elem[0].upper() for elem in list_]
    # # print(list_)
    return str_[0].upper()


class A:
    def f(x):
        print('asdsa')


a = A()
a.f()


@register.filter
def sort(list):
    return {
        'even': [elem for elem in list if elem % 2 == 0],
        'odd': [elem for elem in list if elem % 2 == 1]
    }


@register.filter
def get_value(obj, key):
    return obj.get(key, None)

#
# @register.simple_tag
# def get_categories():
#     return Category.objects.all()


@register.filter
def new_price(old_price, percent):
    print('filter new price', old_price, 'percent', percent)
    if percent != 0.0:
        new_price = percent / 100 * old_price
    else:
        new_price = old_price
    return new_price


# import requests
from django.conf import settings


# @register.simple_tag
# def get_money_exchange_from_NBU():
#     data = requests.get(settings.URI_API_NBU)
#     return data.json()
