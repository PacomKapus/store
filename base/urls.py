from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.Login, name='Login'),
    path('signup/', views.Signup, name='Signup'),
    path('profile/', views.Profile, name='Profile'),
    path('createproduct/', views.Createproductviews, name='Createproduct'),
    path('product/<int:post_id>/', views.Product, name='Product'),
    path('comment/<int:comment_id>/toggle_like/<str:source>/', views.toggle_like, name='toggle_like'),
    path('like/', views.Like, name='Like'), 
    path('catalog/', views.Catalog, name='Catalog'), 
    path('catalog/<str:category>/', views.catalog_by_category, name='catalog_by_category'),
    path('aboutus/', views.Aboutus, name='Aboutus'),  
    path('blog/', views.Blog_views, name='Blog_views'), 
    path('contact/', views.Contact, name='Contact'), 
    path('shipping/', views.Shipping, name='Shipping'), 
    path('bag/', views.Bag, name='Bag'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('search/', views.Search, name='Search'),
    path('delete/<int:blog_id>/', views.delete_blog, name='blog_delete'),
    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),
    path('homedecor/', views.Homedecor, name='Homedecor'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]
