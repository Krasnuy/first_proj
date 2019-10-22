from django.urls import path, include, re_path
from . import views, auth_views

app_name = 'client'
urlpatterns = [
    path('show-book/<int:pk>', views.book_info, name='book-info'),
    path('filters', views.filters, name='filters'),
    path('html', views.html_example),
    path('category-<int:pk>', views.filter_by_category),
    path('cabinet', views.cabinet, name='cabinet'),
    path('return-json', views.return_json),
    # path('login/', auth_views.login_, name='login'),
    # path('logout', auth_views.logout_, name='logout'),
    path('calculator', views.calculator),
    path('demo-model-form', views.demo_model_form, name='demo-model-form'),
    # path('privatbank-api', views.api_privatbank, name='privatbank-api')
]
auth_urls = [
    path('login-form/', auth_views.login_, name='login'),
    path('rgister-form/', auth_views.register_, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.activate, name='activate'),
    path('logout', auth_views.logout_, name='logout'),
]

urlpatterns += auth_urls
