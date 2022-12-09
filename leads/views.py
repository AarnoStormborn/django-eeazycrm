from django.shortcuts import render
from django.http.response import HttpResponse

# List and Detailed view
def leads(request, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        #detailed view
        return HttpResponse(f"Lead {id}")
    # list view
    return HttpResponse("Leads List View")

# Create view
def createLead(request, *args, **kwargs):
    return HttpResponse("Create Lead")

# Update view
def updateLead(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Update Lead: {id}")

# Delete view
def deleteLead(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Delete Lead: {id}")

def convertLead(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Convert Lead: {id}")


