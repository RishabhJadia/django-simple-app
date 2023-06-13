from django.shortcuts import render, redirect

# Create your views here.

def default_page(request):
    return redirect('admin:login')