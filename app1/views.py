from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View




class Home(View):
    template_name = "app1/home.html"
    def get(self,request):
        return render(request, self.template_name)