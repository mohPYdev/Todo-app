import django_filters
from django_filters import CharFilter
from django.forms import TextInput

from .models import Task

class TaskFilter(django_filters.FilterSet):

    title = CharFilter(field_name='title' , lookup_expr='icontains' ,
     widget=TextInput(attrs={
            'placeholder': 'Search', 'class': 'form-control mr-sm-2'})
     )

    class Meta:
        model = Task
        fields = ['title'] 