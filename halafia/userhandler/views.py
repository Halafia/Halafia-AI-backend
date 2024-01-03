from django.shortcuts import render
from .forms import SignUp

# Create your views here.


def signup(request):
    form = signup()

    'form':form
