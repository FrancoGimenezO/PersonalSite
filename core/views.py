from django.shortcuts import render

def home(request):
    return render(request, "core/html/home.html")

def about(request):
    return render(request, "core/html/about.html")

def portfolio(request):
    return render(request, "core/html/portfolio.html")

def blog(request):
    return render(request, "core/html/blog.html")

def contact(request):
    return render(request, "core/html/contact.html")
