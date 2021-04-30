# Django & Django REST framework test project.

Have successfully implemented the API requirement delivering available non blocked listings.


The test links are
 


1 . localhost:8000/listingpagination/ ( for paginated list)


example : http://localhost:8000/listingpagination/?max_price=1000&check_in=2021-6-01&check_out=2021-12-12



2 . localhost:8000/listingfull/ ( full query set)


example : http://localhost:8000/listingfull/?max_price=1000&check_in=2021-6-01&check_out=2021-12-12



Field and Type errors as well as Date format errors are replied with appropriate error messages.

Have used only a single query with filters to deliver the listing to reduce the processing time. Have used bandwidth checking to exclude Listings in blocked days between check_in and check_days from the request. Have included custom functions in model with serializer to deliver Listing items as in the required output. 
A model with Blocked Dates for appartments and hotels is present, and the working of this API depends upon the proper updating of BlockedDates model. Updating of BlockedDates model can be run asynchronously, after every booking with the help of celery and Message brokers like RabbitMq or Redis. Please feel free to go through views and models to dive into the code.


