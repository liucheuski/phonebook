from django.urls import path, re_path

from phonenumbers import views

app_name = 'phonenumbers'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.details, name='details'),
    re_path(r'^register/$', views.RegisterFormView.as_view()),
    re_path(r'^login/$', views.LoginFormView.as_view()),
    re_path(r'^logout/$', views.LogoutView.as_view()),
    re_path(r'^password-change/', views.PasswordChangeView.as_view()),

]
