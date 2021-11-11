from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from militia import models
from militia.forms import TipForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def TipFormView(request):
    context = {}
    if request.method == "POST":
        form = TipForm(request.POST)
        form.save()
        messages.success(request, 'Your anonymous message has been sent!')
    context["form"] = TipForm()
    return render(request, "forms.html", context)