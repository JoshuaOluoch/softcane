from django.urls import path
from . import views
from .views import (login_request,register, logout_request,user_list,
                    UserUpdateView,UserDeleteView,UserDetailView, change_password)



urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_request, name='logout'),
    path('',user_list, name='users'),
    path('<pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<pk>/update/',UserUpdateView.as_view(), name = 'user-update'),
    path('<pk>/delete/',UserDeleteView.as_view(), name = 'user-delete'),
    path('password',change_password, name = 'password-update'),

]
