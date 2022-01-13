
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('card.urls')),
    path('api/v1/', include('order.urls')),
   # path('', include('accounts.urls')),
]
