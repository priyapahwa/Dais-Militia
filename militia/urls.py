from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.resolvers import URLPattern
from militia import views

from militia.views import HomePageView, TipFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("forms/", login_required(views.TipFormView), name="forms"),
]