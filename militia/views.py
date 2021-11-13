from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from militia import models
from militia.forms import TipForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class FaqPageView(TemplateView):
    template_name = "faq.html"


def TipFormView(request):
    if request.method == "POST":
        form = TipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your anonymous message has been sent!")
        else:
            messages.error(request, "Enter valid information")
    return render(request, "forms.html")
