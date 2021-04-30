from listings.models import BookingInfo, HotelRoomType, HotelRoom, Listing, BlockedDays
from rest_framework import serializers



class ListingAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingInfo
        fields = ['listing_type','title','country','city','price']

