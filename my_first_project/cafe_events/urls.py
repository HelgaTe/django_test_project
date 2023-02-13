
from django.urls import path
from .views import events, list_events_year, list_events_year_month

urlpatterns = [
    path('', events),
    path('<int:year>/', list_events_year),
    path('<int:year>/<int:month>/', list_events_year_month)
]