from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from . import forms
# Create your views here.

class Signup(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
