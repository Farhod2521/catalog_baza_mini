from django.urls import path
from .views import ElonBazaListView

urlpatterns = [
    path('elon-baza/', ElonBazaListView.as_view(), name='elon-baza-list'),
]
