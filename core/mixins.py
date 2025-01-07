from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import AccessMixin

# this is responsible for monitoring request activity e.g. blacklisting etc
class MonitorAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        # TODO: monitor based on request data
        return super().dispatch(request, *args, **kwargs)