from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from core.mixins import MonitorAccessMixin
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

# class LoginView(View, MonitorAccessMixin):
#     template_name = "auth_app/login.html"
#     context_data = {}
    
#     def get(self, request):
#         self.context_data["form"] = LoginForm()
#         return render(request=request, template_name=self.template_name, context=self.context_data)
    
#     def post(self, request):
#         form = LoginForm(request, request.POST)
#         username = request.POST.get("username")
#         password = request.POST.get("password")
        
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 messages.add_message(request, messages.SUCCESS, _("Successfully logged in as" + f" {user.username}."))
#                 login(request, user)
#                 if request.GET.get("next"):
#                     return redirect(next)
#                 return redirect(reverse_lazy("tracker:home"))
            
#         # if form.is_valid():
#         #     user = form.get_user()
#         #     login(request, user)
#         #     messages.add_message(request, messages.SUCCESS, _("Successfully logged in as" + f" {user.username}."))

#         #     if request.GET.get("next"):
#         #         return redirect(next)
#         #     return redirect(reverse_lazy("tracker:home"))

#         messages.add_message(request, messages.ERROR, _("Invalid credentials provided!"))
#         self.context_data["form"] = LoginForm()
#         return render(request=request, template_name=self.template_name, context=self.context_data)
    
def logout_view(request):
    messages.success(request, f'{request.user} successfully logged out.')
    logout(request)
    return redirect(reverse_lazy("auth_app:login"))



def login_view(request):
    if request.user.is_authenticated:
        return redirect("tracker:home")

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password:
                user = authenticate(request, username=username, password=password)
                # Check if authentication is successful
                if user is not None:
                    login(request, user)
                    if request.GET.get("next"):
                        return redirect(next)
                    return redirect(reverse_lazy("tracker:home"))
                else:
                    messages.error(request, "Invalid username or password provided.")
            else:
                messages.error(request, "Username and password must be provided.")
        else:
            messages.error(request, "Invalid username or password provided. Please try again.")
    else:
        form = LoginForm()

    # Ensure the form is always rendered if the conditions above don't redirect
    return render(request, 'auth_app/login.html', {'form': form})
