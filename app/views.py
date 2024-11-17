from django.shortcuts import render
from django.contrib import messages
from app.models import File, Company_data
import pandas as pd
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm
import math

# Create your views here.

def index(request):
    return render(request, 'app/profile.html')


def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    print('DF:....',df)
    print('DF_KEYS:....',df.keys)
    print('df_values...',df.values)
    # df['year_founded'] = df['year_founded'].apply(lambda x: 0 if pd.isna(x) else int(x))
    df['year_founded'] = df['year_founded'].apply(lambda x: 0 if pd.isnan(x) else int(x))
    list_of_csv = [list(row)  for row in df.values]
    for l in list_of_csv:
        Company_data.objects.create(
            id = l[0],
            name = l[1],
            domain = l[2],
            year_founded = l[3],
            industry = l[4],
            size_range = l[5],
            locality = l[6],
            country = l[7],
            linkedin_url = l[8],
            current_employee_estimate = l[9],
            total_employee_estimate = l[10],
        )

@login_required
def upload_data(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db(obj.file)
        messages.success(request,'File Uploaded successfully!!!')
    return render(request, 'app/upload_data.html')

@login_required
def query_builder(request):
    if request.method == 'POST':
        ef = request.POST['id1']
        et = request.POST['id2']
        nm = request.POST['name']
        ind = request.POST['industry']
        yf = request.POST['year_founded']
        ct = request.POST['city']
        st = request.POST['state']
        con = request.POST['country']
        if ef and et:
            Employee = Company_data.objects.filter(Q(id__gte=ef)&Q(id__lte=et))
        elif nm:
            Employee = Company_data.objects.filter(name=nm)
        elif ind:
            Employee = Company_data.objects.filter(industry__icontains=ind)
        elif yf:
            Employee = Company_data.objects.filter(year_founded__exact=yf)
        elif ct:
            Employee = Company_data.objects.filter(locality__icontains=ct)
        elif st:
            Employee = Company_data.objects.filter(locality__icontains=st)
        elif con:
            Employee = Company_data.objects.filter(country__icontains=con)  
        count = Employee.count()
        print(count)    
        messages.success(request,f'{count} Records found for the query')
    return render(request, 'app/query_builder.html', locals())

def login(request):
    return render(request, 'app/login.html')


def logout(request):
    form = LoginForm()
    return render(request, 'app/logout.html',locals())

@login_required
def User_show(request):
    users = User.objects.all()
    return render(request, 'app/users.html',{'users':users})

        