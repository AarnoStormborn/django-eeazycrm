from django.shortcuts import render
from django.http.response import HttpResponse

# List and Detailed view
def deals(request, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        #detailed view
        return HttpResponse(f"Deal {id}")
    # list view
    return HttpResponse("Deals List View")

# Create view
def createDeal(request, *args, **kwargs):
    return HttpResponse("Create Deal")

# Update view
def updateDeal(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Update Deal: {id}")

# Delete view
def deleteDeal(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Delete Deal: {id}")

