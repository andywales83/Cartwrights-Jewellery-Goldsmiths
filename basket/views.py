from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view that returns the shopping basket page for the user """

    return render(request, 'basket/basket.html')
