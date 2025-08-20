from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "user/dashboard.html"
    login_url = 'login'

class RegisterView(FormView):
    template_name = "user/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # this saves the user including all fields
        return super().form_valid(form)