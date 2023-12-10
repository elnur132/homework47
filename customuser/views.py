from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUserForm, AskForm
from .models import CreateUser
from .utils import CustomLoginRequiredMixin

from django.contrib.auth import REDIRECT_FIELD_NAME

from django.conf import settings


class Mistake(TemplateView):
    template_name = 'mistake.html'

class DashBoard(CustomLoginRequiredMixin,ListView):
    model = CreateUser
    template_name = 'dashboard.html'
    context_object_name = 'users'
    
class CreateUserView(CreateView):
    model = CreateUser
    form_class = CreateUserForm
    template_name = 'createuser.html'
    success_url = reverse_lazy('dashboard')
    
class DetailUserView(DetailView):
    model = CreateUser
    form_class = AskForm
    pk_url_kwarg = 'user_id'
    template_name = 'user_detail.html'
    context_object_name = 'user'
    success_url = reverse_lazy()
    
    def form_valid(self, form):
        # Получите текущего пользователя
        current_user = self.request.user
        if form:
            current_user.save()
        return super().form_valid(form)
    
class UserLogin(LoginView):
    template_name = 'createuser.html'
    next_page = reverse_lazy('dashboard')

class UserLogoutView(LogoutView):
    next_page = 'login'
    