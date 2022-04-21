import users.models
from .models import User
from .forms import NewUserForm, CustomUserChangeForm
from tenant.utilities import get_tenant
from tenant.models import Tenant

from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


# User = get_user_model()
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="users/login.html",
                  context={"form": form})


# Logout view
@login_required()
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


# Register User View
@login_required()
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect("users")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="users/register.html",
                          context={"form": form})

    form = NewUserForm()
    return render(request=request,
                  template_name="users/register.html",
                  context={"form": form})


# User List View
@login_required()
def user_list(request):
    tenant = get_tenant(request)
    users = User.objects.filter(tenant=tenant)
    return render(request, 'users/users.html', {'users': users, 'tenant': tenant})


# User Detail View
class UserDetailView(LoginRequiredMixin, ListView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(User, pk=kwargs['pk'])
        context = {'object': object}
        return render(request, 'users/user_detail.html', context)


# Update User
class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'users/user_update.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users')

    # @property
    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(User, user_id=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


# User Delete
class UserDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(User, pk=pk_)


# Change Password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'users/change_password.html', {'form': form})


