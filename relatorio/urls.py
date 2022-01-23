from unicodedata import name
from django.urls import path
from .views import IndexView, Index2View

urlpatterns = [
    path('relatorio/', IndexView.as_view(), name='index'),
    path('relatorio2/', Index2View.as_view(), name='index2'),
]

