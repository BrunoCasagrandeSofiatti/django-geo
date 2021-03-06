from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView, DadosJSONView

urlpatterns = [
    path('chartjs/', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
]
