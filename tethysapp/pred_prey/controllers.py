from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button

@controller
def home(request):
    """
    Controller for the app home page.
    """
    context = {}
    return render(request, 'pred_prey/home.html', context)