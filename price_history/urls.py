"""price_history URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_view
from products.views import ProductDetailView,ProductDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laptops/',product_view.laptops,name='Laptops'),
    path('mobiles/',product_view.phones,name='Mobile Phones'),
    path('headphones/',product_view.headphones,name='Headphones'),
    path('tablets/',product_view.tablets,name='Tablets'),
    path('details/',product_view.productDetailView,name='all-products'),
    path('details/<str:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('prods/<str:pk>/',product_view.prod_detail,name='new-product-detail'),
    path('prods/<str:pk>/<int:time_frame>/',product_view.graph_detail,name='new-graph-detail'),
    path('product/<str:pk>/delete',ProductDeleteView.as_view(),name="product-delete"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),name='password_reset_complete'),
    path('',include('users.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
