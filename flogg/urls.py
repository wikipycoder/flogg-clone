from django.urls import path
from . import views


urlpatterns = [

    path("products", views.ProductAPIView.as_view(), name="products"),
    path("categories", views.CategoryAPIView.as_view(), name="categories"),
    path("brands", views.BrandAPIView.as_view(), name="brands"),
    path("details", views.DetailAPIView.as_view(), name="details")
]