from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button

@controller
def home(request):
    """
    Controller for the app home page.
    """
    context = {
        'initial_x0': 100,
        'initial_y0': 100,
        'initial_alpha': 0.005,
        'initial_beta': 0.00005,
        'initial_delta': 0.00007,
        'initial_gamma': 0.002,
    }
    return render(request, 'pred_prey/home.html', context)