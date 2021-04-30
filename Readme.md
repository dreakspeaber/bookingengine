# Django & Django REST framework test project.

Have successfully implemented the API requirement delivering available non blocked listings.


The test links are
 


1 . localhost:8000/listingpagination/ ( for paginated list)


example : http://localhost:8000/listingpagination/?max_price=1000&check_in=2021-6-01&check_out=2021-12-12



2 . localhost:8000/listingfull/ ( full query set)


example : http://localhost:8000/listingfull/?max_price=1000&check_in=2021-6-01&check_out=2021-12-12



Field and Type errors as well as format errors are replied with appropriate error messages.

Have used only a single query argument to deliver the listing with least processing time. Please feel free to go through views and models to dive into the code.


