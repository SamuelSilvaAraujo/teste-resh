from django.views.generic import TemplateView



class ProfileView(TemplateView):
    template_name = "profile.html"

class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class ChangeUserView(TemplateView):
    template_name = "change_user.html"
