"""
URL configuration for order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Main_page.views as main_views
import Shopping_cart_page.views as cart_views
import Сontact_page.views as contact_page_views
import Product_page.views as product_page_views
import Authorization_Registration.views as authorization_reg_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_views.main, name = 'main'),
    path("shopping_cart_page/", cart_views.shopping_cart_page, name = "shopping"),
    path("contact_page_/", contact_page_views.contact_page, name = 'contacts'),
    path("product_page/", product_page_views.product_page, name = 'products'),
    path("auth/", authorization_reg_views.auth, name="auth"),
    path("reg/", authorization_reg_views.reg, name="reg"),
]
