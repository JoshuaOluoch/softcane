from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from accounting.models import *
from tenant.models import TenantAwareModel
from users.models import User
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div
from crispy_forms import bootstrap, layout
from django.urls import reverse
from crispy_forms.layout import Layout, Submit


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.CheckboxInput()

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email','role', 'department', 'designation', 'is_active')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Register', css_class='btn-primary'))



    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('username', css_class="col-sm-4"),
                    Div('fullname', css_class="col-sm-4"),
                    Div('email', css_class="col-sm-4"),
                    css_class='row',
                ),
                Div(
                    Div('role', css_class="col-sm-3"),
                    Div('department', css_class="col-sm-3"),
                    Div('designation', css_class="col-sm-3"),
                    Div('is_active', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Update', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("users")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )

        )

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email','role', 'department', 'designation', 'is_active')


class AdminUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email','role', 'department', 'designation', 'is_active', 'tenant')

    def save(self, commit=True):
        user = super(AdminUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'role','department', 'designation', 'is_active', 'tenant')
