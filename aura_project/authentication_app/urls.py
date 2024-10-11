from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/',views.register_view,name = 'sign_up'),
    path('login/',views.login_view,name='login'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('resend_otp/',views.resend_otp_view,name='resend_otp'),
]