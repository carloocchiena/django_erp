from django.shortcuts import render
from django.views import View

from . import models

class Home(View):
    def get(self, request):
        return render(request, 'base.html')
