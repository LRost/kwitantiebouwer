from django.urls import path
from . import views

urlpatterns = [
    path('nieuwe-kwitantie', views.nieuwe_kwitantie, name='nieuw_kwitantie'),
    path('', views.KwitantieListView.as_view(), name='kwitantie-list'),
    path('<int:pk>', views.get_pdf, name='kwitantie-detail'),
    ]


