from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import PlotlyView
from .pred_prey import run_pred_prey_simulation, generate_population_dynamics_plot, generate_phase_space_plot

@controller
def home(request):
    """
    Controller for the app home page.
    """
    x0 = 10  # fish units in hudreds
    y0 = 1  # bears units in hudreds
    alpha = 1.1
    beta = 0.4
    delta = 0.1
    gamma = 0.4
    
    # Handle form submission
    if request.POST and 'update-plots-submit' in request.POST:
        # Update values from values given by user in the form
        x0 = int(request.POST.get('x0', x0))
        y0 = int(request.POST.get('y0', y0))
        alpha = float(request.POST.get('alpha', alpha))
        beta = float(request.POST.get('beta', beta))
        delta = float(request.POST.get('delta', delta))
        gamma = float(request.POST.get('gamma', gamma))

    # Run simulation
    t, z = run_pred_prey_simulation(x0, y0, alpha, beta, delta, gamma)

    # Population dynamics plot
    pop_dyanmics_fig = generate_population_dynamics_plot(t, z)
    pop_dyanmics_plot = PlotlyView(pop_dyanmics_fig)
    
    # Phase space plot
    phase_space_fig = generate_phase_space_plot(z)
    phase_space_plot = PlotlyView(phase_space_fig)
    
    context = {
        'initial_x0': x0,
        'initial_y0': y0,
        'initial_alpha': alpha,
        'initial_beta': beta,
        'initial_delta': delta,
        'initial_gamma': gamma,
        'pop_dynamics_plot': pop_dyanmics_plot,
        'phase_space_plot': phase_space_plot,
    }
    return render(request, 'pred_prey/home.html', context)