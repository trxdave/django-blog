from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import About


def about_view(request):
    about_instance = About.objects.first()
    return render(request, 'about/about.html', {'about': about_instance})