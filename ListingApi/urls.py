from django.views.generic import TemplateView
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
# from house.admin import betoch_admin
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import LandingView
from subscriber.views import Subscribe


urlpatterns = [
    
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token-refresh-obtain-pair'),
    path('admin/', admin.site.urls),  
    path('api/v1/subscribe/', Subscribe.as_view(),name = 'subscribe'),
    # path('api/v1/house/', include('house.urls')),
    path('api/v1/realtors/', include('realtors.urls')),
    path('api/v1/listings/', include('listings.urls') ,name = "listing"),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/pay/', include('payments.urls')),
    path('api/v1/favs/', include('favorites.urls')),
    path('api/v1/servicefee/', include('ServiceFee.urls')),
    path('landing/', LandingView,name = "landing"),
    # path('api/v1/profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name = "index.html"),name = "index")]

