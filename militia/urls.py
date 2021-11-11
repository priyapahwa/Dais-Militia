from django.urls import path
from django.urls.resolvers import URLPattern

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]