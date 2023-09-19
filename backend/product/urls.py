from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsListAPIView.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailAPIView.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetailAPIView.as_view()),
]
