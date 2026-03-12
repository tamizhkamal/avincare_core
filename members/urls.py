from django.urls import include, path

from members import views

urlpatterns = [
    path('', views.members, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('vision/', views.vision, name='vision'),
    path('board/', views.board, name='board'),
    path('quality/', views.quality, name='quality'),
    path('products/', views.products, name='products'),
    path('responsibility/', views.responsibility, name='responsibility'),
    path('company/', views.company, name='company'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('contact/', views.contact, name='contact'),
]
