from django.shortcuts import render
from app.models import File, Company_data
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')


def upload_data(request):
    if request.method == 'POST':
        file = request.FILES['file']
        File.obj.create(file=file)
    return render(request, 'app/upload_data.html')


def query_builder(request):
    return render(request, 'app/query_builder.html')


def login(request):
    return render(request, 'app/query_builder.html')


def logout(request):
    return render(request, 'app/query_builder.html')