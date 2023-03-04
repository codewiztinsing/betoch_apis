from django.urls import path
from .views import (
	ListingsView,
	ListingView,
	SearchView,
	ListingCreateView,
	router,
	RelatedSearchView,
	useraddlisting,
	AddandRetrieveFavoriteView,
	MYListing,
	FullTextSearch,
	MyListingsView,
	mylistings

	)


app_name = "listing"

urlpatterns = [
	path('search/',SearchView.as_view(),name = 'listing'),
	path('full-search/',FullTextSearch.as_view(),name = 'full-search'),
	path('add-favorite/',AddandRetrieveFavoriteView.as_view(),name = 'add-favorite'),
	path('remove-favorite/',AddandRetrieveFavoriteView.as_view(),name = 'remove-favorite'),
	path('favorites/',AddandRetrieveFavoriteView.as_view(),name = 'remove-favorite'),
	path('related_search/',RelatedSearchView.as_view(),name = 'listing-related'),
	path('create/',ListingCreateView.as_view(),name = 'listing-create'),
	path('user-add/',useraddlisting,name = 'user-add'),
	# path('mylistings/',MYListing.as_view(),name = 'mylistings'),
	path('mylistings/',mylistings,name = 'mylisting'),
	path('realtorlisting/',MyListingsView.as_view(),name = 'mylistingrealtorview'),
	path('<slug>/',ListingView.as_view(),name = 'listing'),
	
]
urlpatterns += router.urls