from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileView(TemplateView):
    template_name = "profile.html"

class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"
