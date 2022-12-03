from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from django.urls import reverse
# Create your views here.
from .models import Car

from . import forms

class CarsParsed(ListView):
    model = Car
    template_name = "parser/cars_list.html"

    def get_queryset(self):
        return Car.objects.all()

class CarsParserFormView(FormView):
    template_name = 'parser/car_parsed.html'
    form_class = forms.CarParseForm

    def post(self, request, *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            a = form.parser_data()
            
            if a == 1:
                return render(request,'parser/after_parse.html',context={'data':True})
            else:            
                return render(request,'parser/after_parse.html',context={'data':False})
        else:
            return super(CarsParserFormView,self).post(request,*args,**kwargs)