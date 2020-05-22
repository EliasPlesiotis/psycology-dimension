from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response


class register(View):
    form_class = forms.NewUserForm
    template_name = 'accounts/register.html'

    def get(self, req, *args, **kwargs):
        form = self.form_class()
        return render(req, self.template_name, {'form': form})
    
    def post(self, req, *args, **kwargs):
        form = self.form_class(req.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                form.save()
                return redirect('http://localhost:3000/')
            else:
                return render(req, self.template_name, {'form': form, 'errors': form.errors})
        else: 
            return render(req, self.template_name, {'form': self.form_class()})

class get_id(views.APIView):
    def get(self, req, *args, **kwargs):
        user = req.user
        return Response({'id': user.id, 'username': user.username})