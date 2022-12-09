from django.shortcuts import render
from django.http.response import HttpResponse

# List and Detailed view
def contacts(request, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        #detailed view
        return HttpResponse(f"Contact {id}")
    # list view
    return HttpResponse("Contacts List View")

# Create view
def createContact(request, *args, **kwargs):
    return HttpResponse("Create Contact")

# Update view
def updateContact(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Update Contact: {id}")

# Delete view
def deleteContact(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Delete Contact: {id}")
