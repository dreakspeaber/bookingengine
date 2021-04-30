from listings.models import BookingInfo
from listings.serializers import ListingAvailabilitySerializer
from rest_framework import generics,pagination,views 
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime


#Error messages for field and dateformat errors
FIELD_ERROR = 'Please make sure that all variables are present and spelled correctly. Here is a sample for you http://localhost:8000/list/?mx_price=1000&check_in=2021-3-10&check_out=2021-4-2'
DATE_FORMAT_ERROR = 'Date format is wrong. Try YYYY-MM-DD format'


#Pagination for paginated JSON listviews
class ListPagination(pagination.PageNumberPagination):
    page_size = 8  





#The Query returns a list of items with price less than or equal to the max_price.
#which further is filtered by excluding hotel_room_type and apartments with date
#coinciding with the user requested check_in and check_out dates. By combining the query in a single search,
# we can very well increase the API response time.
#The error variable checks for potential errors in the request format and gives, appropriate suggestions to correct the request.
# The first try and except looks for potential field error, and the second try identifies format error in datestring.


class ListingListPagination(generics.ListAPIView):
    serializer_class = ListingAvailabilitySerializer
    pagination_class = ListPagination

    
    def get_queryset(self):
        self.error=0
        check_in = self.request.GET.get('check_in',None)
        check_out = self.request.GET.get('check_out',None)
        price = self.request.GET.get('max_price',None)
        if((check_in is None) or (check_out is None) or (price is None)):
            self.error=1
            return []
        try:
            return BookingInfo.objects.filter(price__lte=int(price)).exclude(\
                Q(Q(blocked_days__start_date__gte=check_in) & Q(blocked_days__start_date__lt=check_out)) or \
                    Q(Q(blocked_days__end_date__gt=check_in) & Q(blocked_days__end_date__lte=check_out)))\
                        .order_by('price')
        except:
            self.error=2
            return []



    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if self.error==1:
            response.data['status'] = 400
            response.data['message'] = FIELD_ERROR
        if self.error==2:
            response.data['status'] = 400
            response.data['message'] = DATE_FORMAT_ERROR
        return response








#To see full list of items. Not advisable for huge datasets


class ListingListFull(views.APIView):
    def get(self,request):
        check_in = self.request.GET.get('check_in',None)
        check_out = self.request.GET.get('check_out',None)
        price = self.request.GET.get('max_price',None)
        if((check_in is None) or (check_out is None) or (price is None)):
            response = {
                'status' : 400,
                'message': FIELD_ERROR,
            }
            return Response(response)

        try:
            data = BookingInfo.objects.filter(price__lte=price).exclude(\
                Q(Q(blocked_days__start_date__gte=check_in) & Q(blocked_days__start_date__lt=check_out)) or \
                    Q(Q(blocked_days__end_date__gt=check_in) & Q(blocked_days__end_date__lte=check_out)))\
                        .order_by('price')
            ser = ListingAvailabilitySerializer(data,many=True)
            response = {
                'items' : ser.data
            }
        except:
            response = {
                'status' : 400,
                'message': DATE_FORMAT_ERROR,
            }
        
        return Response(response)

