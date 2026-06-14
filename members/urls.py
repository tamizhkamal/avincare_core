from django.urls import include, path
from django.views.generic import RedirectView

from members import views
from members import contact_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', RedirectView.as_view(url='/', permanent=False)),
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
    path('contact/', contact_views.contact, name='contact'),
    path('contact-form/', contact_views.contact_form, name='contact_form'),

    #Admin Dashboard
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('board_of_directors/', views.board_of_directors, name='board_of_directors'),
    path('products_page/', views.products_page, name='products_page'),
    
    # API Endpoints
    path('api/add-director/', views.add_director, name='add_director'),
    path('api/get-director/<int:director_id>/', views.get_director, name='get_director'),
    path('api/update-director/<int:director_id>/', views.update_director, name='update_director'),
    path('api/delete-director/<int:director_id>/', views.delete_director, name='delete_director'),
    path('api/add-product/', views.add_product, name='add_product'),
    path('api/get-product/<int:product_id>/', views.get_product, name='get_product'),
    path('api/update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('api/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]
