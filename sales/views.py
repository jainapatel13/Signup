from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext

from sales.models import Sale
from sales.forms import SalePaymentForm

from django.template.context_processors import csrf


def charge(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        form = SalePaymentForm(request.POST)
        
        if form.is_valid(): # charges the card
            print("done!!!!!")
            return render(request, "charge.html", {'form': form},c)
    else:
        form = SalePaymentForm()
    
    return render(request, "charge.html",
                              {'form': form})



def charges(request):
    form = SalePaymentForm()
    return render_to_response("charge.html",
                              {'form': form})
