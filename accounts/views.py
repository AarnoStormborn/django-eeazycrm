from django.shortcuts import render
from django.http.response import HttpResponse

# List and Detailed view
def accounts(request, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        #detailed view
        return HttpResponse(f"Account {id}")
    # list view
    return HttpResponse("Accounts List View")

# Create view
def createAccount(request, *args, **kwargs):
    return HttpResponse("Create an Account")

# Update view
def updateAccount(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Update Account: {id}")

# Delete view
def deleteAccount(request, *args, **kwargs):
    id = kwargs.get('id')
    return HttpResponse(f"Delete Account: {id}")