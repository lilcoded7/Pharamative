from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.shop, name='food'),
    path('cart/', views.cart, name='cart'), 
    path('update-item/', views.updateItem, name='update-item'),
    path('process-order/', views.process_order, name='process-order'),
    path('about/', views.about, name='about'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
    path('customer/dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin-dashboard'),
    # path('qrcode/reader/', views.read_qr_code, name='qr_code_reader')
    path('scan/qrcode/', views.scan_qrcode),
    path('food/menu/<int:pk>/', views.food_menu_view, name='menu'),
    path('search/food/', views.search_food, name='search'),
    path('delete/order', views.delete_order, name='delete-order')

]   

