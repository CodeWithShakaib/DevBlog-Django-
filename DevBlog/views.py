from django.http import HttpResponse


def initial(request):
    return HttpResponse("<h2 style='border:1px solid lightgrey;padding:50px;background:grey;color:white;align:center;'>This is the view Handled by main project <h2>.")