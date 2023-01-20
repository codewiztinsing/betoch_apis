from django.urls import path
from .views import ListingsView,ListingView,SearchView,ListingCreateView
urlpatterns = [
	path('',ListingsView.as_view(),name = 'listings'),
	path('search/',SearchView.as_view(),name = 'listing'),
	path('create/',ListingCreateView.as_view(),name = 'listing-create'),
	path('<slug>/',ListingView.as_view(),name = 'listing'),
	
]