from django.urls import path
from .views import RealtorListView,RealtorView,TopSellerView,RealtorCreateView,RealtorUpdateView,RealtorViewWithPk
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('',RealtorListView.as_view(),name = 'realtors'),
	path('update/',RealtorUpdateView.as_view(),name = 'realtor-update'),
	path('create/',RealtorCreateView.as_view(),name = 'realtor-create'),
	path('<email>/',RealtorView.as_view(),name = 'realtor'),
	path('realtor/<pk>/',RealtorViewWithPk.as_view(),name = 'realtor'),
	path('top-sellers/',TopSellerView.as_view(),name = 'top-realtors'),
]


