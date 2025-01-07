from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from core.mixins import MonitorAccessMixin
from auth_app import forms as AuthAppForms
from django.contrib.auth import login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class LoginView(View, MonitorAccessMixin):
    template_name = "auth_app/login.html"
    context_data = {}
    
    def get(self, request):
        self.context_data["form"] = AuthAppForms.LoginForm()
        return render(request=request, template_name=self.template_name, context=self.context_data)
    
    def post(self, request):
        form = AuthAppForms.LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, _("Successfully logged in as" + f" {user.username}."))

            if request.GET.get("next"):
                return redirect(next)
            return redirect(reverse_lazy("tracker:home"))
        
        messages.add_message(request, messages.ERROR, _("Invalid credentials provided!"))
        self.context_data["form"] = AuthAppForms.LoginForm()
        return render(request=request, template_name=self.template_name, context=self.context_data)
    
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("auth_app:login"))