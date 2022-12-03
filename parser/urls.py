from django.urls import path
from . import views

app_name = "parser"

urlpatterns = [
    path('',views.CarsParsed.as_view(), name="cars_list"),
    path('info/',views.CarsParserFormView.as_view(), name="car_info")
]
