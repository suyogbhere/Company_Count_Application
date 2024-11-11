from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def upload_data(request):
    return render(request, 'app/upload_data.html')


def query_builder(request):
    return render(request, 'app/query_builder.html')


def login(request):
    return render(request, 'app/query_builder.html')


def logout(request):
    return render(request, 'app/query_builder.html')