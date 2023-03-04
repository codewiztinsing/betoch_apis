from .views import router
from django.urls import path
from .views import PayServiceView


urlpatterns = [
	path('pay/',PayServiceView.as_view(),name = "pay"),

]
urlpatterns += router.urls