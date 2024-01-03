from django.shortcuts import render, HttpResponse
from .halafia import generatie_risk_assessment

# Create your views here.

def index(request):
    return render(request, "index.html")
