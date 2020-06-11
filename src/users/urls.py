from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('apilogin/', UserLoginView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('details/', UserDetails.as_view(), name='details'),
    path('upload/', FileUploadView.as_view()),
    path('time/', ScreenTimeView.as_view(), name="time"),
    path('delete/<int:id>/', Delete_images.as_view(), name='delete'),
    path('delete_action', MultipleDelete.as_view(), name='delete'),
    path('delete_user/<int:id>/', DeleteUser.as_view(), name='delete_user'),
    path('stats/<int:id>/', UserStats.as_view(), name='stats'),

    path('images/<int:id>/<int:month>/<int:date>/<int:year>/', UserImages.as_view(),
         name='images'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='main_app/forgot-password.html'),
         name='forgot_password'),
    path('settings/', Admin_settings.as_view(), name='settings'),
    path('404/', TemplateView.as_view(template_name="main_app/404.html"), name='404'),

]
