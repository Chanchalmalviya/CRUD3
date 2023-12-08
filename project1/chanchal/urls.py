from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path("", views.index),
    path("regi_views/",views.regi_views),
    path("ragistration/",views.ragistration),
    path("login/",views.login),
    path("product/",views.product),
    path("view_add_product/",views.view_add_product),
    path("add_product/",views.add_product),
    path("delete/<int:pk>/",views.delete_product,name="delete"),
    path("productupdate/<int:uid>/",views.productupdate,name="productupdate"),
    path("update/",views.Product_update,name="update"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
