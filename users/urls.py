from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'


urlpatterns = [
    # Login and out url
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # Regestration
    path('register/', views.register, name='register'),
    # user account edit
    path('edit/', views.edit, name='edit'),
    # Dashbord url
    path('', views.dashboard, name='dashboard'),
    # Settings
    path('settings/', views.settings, name='settings'),
    # Delete account
    path('delete_account/', views.delete_account, name='delete_account'),
]
