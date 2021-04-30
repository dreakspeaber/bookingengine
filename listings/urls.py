from django.urls import path
from listings import views

urlpatterns = [
     
    
    path('listingpagination/',views.ListingListPagination.as_view()), #pagination url
    path('listingfull/',views.ListingListFull.as_view()), #full list url

]