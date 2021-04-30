from django.db import models


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)

    def __str__(self):
        return self.title
    

class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_room_types'
    )
    title = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.hotel} - {self.title}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_rooms'
    )
    room_number = models.CharField(max_length=255,)

    def __str__(self):
        return self.room_number


class BookingInfo(models.Model):
    listing = models.OneToOneField(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )
    hotel_room_type = models.OneToOneField(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type
            
        return f'{obj} {self.price}'



#functions to produce JSONfield data for Available Listings

    def title(self):
        if self.listing:
            return self.listing.title
        else:
            return self.hotel_room_type.hotel.title


    def listing_type(self):
        if self.listing:
            return "Apartment"
        else:
            return "Hotel"


    def country(self):
        if self.listing:
            return self.listing.country
        else:
            return self.hotel_room_type.hotel.country


    def city(self):
        if self.listing:
            return self.listing.city
        else:
            return self.hotel_room_type.hotel.city





class BlockedDays(models.Model):
    BookingInfo = models.ForeignKey(
        BookingInfo,
        on_delete=models.CASCADE,
        related_name='blocked_days',
    )
    start_date = models.DateField()    #check_in date
    end_date = models.DateField()      #check_out date


    def __str__(self):
        if self.BookingInfo.listing:       
            return f'{self.BookingInfo.listing.title} {self.start_date} {self.end_date}'
        
        else:
            return f'{self.BookingInfo.hotel_room_type.title} {self.start_date}  {self.end_date}'
