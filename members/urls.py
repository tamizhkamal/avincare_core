from django.urls import include, path

from members import views

urlpatterns = [
    path('', views.members, name='members'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('service/', views.service, name='service'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]
