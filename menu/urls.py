



from django.urls import path
from . import views 

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('get-products/<int:category_id>/', views.get_products_by_category, name='get_products_by_category'),
]

