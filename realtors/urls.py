from django.urls import path
from .views import RealtorListView,RealtorView,TopSellerView,RealtorCreateView
urlpatterns = [
	path('',RealtorListView.as_view(),name = 'realtors'),
	path('create/',RealtorCreateView.as_view(),name = 'realtor-create'),
	path('<email>/',RealtorView.as_view(),name = 'realtor'),
	path('top-sellers/',TopSellerView.as_view(),name = 'top-realtors'),
]

