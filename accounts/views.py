from django.shortcuts import render
from . import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.CreateUserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
