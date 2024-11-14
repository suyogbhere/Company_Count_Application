import django_filters
from app.models import *
from django import forms


class Company_data_filter(django_filters.FilterSet):
    id = django_filters.ModelChoiceFilter(
        queryset= Company_data.objects.all(),
        field_name='id',
        label = 'Employees(From)',
        lookup_expr= 'gte',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Employees(From)'}))

    id = django_filters.ModelChoiceFilter(
        queryset= Company_data.objects.all(),
        field_name='id',
        label = 'Employees(to)',
        lookup_expr= 'lte',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Employees(to)'}))

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Keyword'}))
    
    industry = django_filters.ModelChoiceFilter(
        queryset= Company_data.objects.all(),
        field_name='industry',
        lookup_expr='icontains',
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'industry'}))
    
    year_founded = django_filters.ModelChoiceFilter(
        queryset= Company_data.objects.all(),
        field_name='year_founded',
        lookup_expr='exact',
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'year_founded'}))
    
    locality = django_filters.ModelChoiceFilter(
        queryset= Company_data.objects.all(),
        field_name='locality',
        lookup_expr='icontains',
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'locality'}))
    
    class Meta:
        model = Company_data
        fields = ['id','name','industry','year_founded','locality','country']






    # cdfilter = Company_data_filter(request.POST, queryset = cd)
    # cd = cdfilter.qs
    # count = cd.count()
    # print(count)
    # context={
    #     'cd':cd, 'cdfilter':cdfilter
    # }