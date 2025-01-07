from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import MonitorAccessMixin

class HomeView(MonitorAccessMixin, LoginRequiredMixin, View):
    template_name = "tracker/index.html"
    context_data = {}

    def get(self, request):
        return render(request=request, template_name=self.template_name, context=self.context_data)