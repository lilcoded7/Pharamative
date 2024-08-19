from django.urls import path 
from account import views

 
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/customer/code/', views.verify_customer_email_code, name='verify-customer-code'),
    path('verify/customer/email/', views.send_email_verify_code, name='verify-customer-email'),
    path('reset/password/', views.reset_password, name='password-reset'),
    path('send_reset_password_email_verify_code/', views.send_reset_password_email_verify_code, name='reset-password-email'),
]