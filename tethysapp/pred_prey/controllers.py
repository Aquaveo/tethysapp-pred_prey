from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import PlotlyView, SelectInput
from .pred_prey import run_pred_prey_simulation, generate_population_dynamics_plot, generate_phase_space_plot


SCENARIOS = {
        'bears-and-fish': {
            'name': 'Bears and Fish',
            'alpha': 1.1,
            'beta': 0.4,
            'delta': 0.1,
            'gamma': 0.4,
        },
        'foxes-and-rabbits': {
            'name': 'Foxes and Rabbits',
            'alpha': 1.7,
            'beta': 0.6,
            'delta': 0.2,
            'gamma': 0.3,
        },
        'wolves-and-sheep': {
            'name': 'Wolves and Sheep',
            'alpha': 1.5,
            'beta': 0.8,
            'delta': 0.1,
            'gamma': 0.1,
        },
        'velociraptor-and-guests': {
            'name': 'Velociraptor and Park Guests',
            'alpha': 1.2,
            'beta': 0.9,
            'delta': 0.3,
            'gamma': 0.2,
        },
    }

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
    scenario = 'bears-and-fish'

    has_errors = False
    x0_error = ""
    y0_error = ""
    alpha_error = ""
    beta_error = ""
    delta_error = ""
    gamma_error = ""

    # Handle form submission
    if request.POST and 'update-plots-submit' in request.POST:
        # Update values from values given by user in the form
        x0 = int(request.POST.get('x0', x0))
        y0 = int(request.POST.get('y0', y0))
        alpha = float(request.POST.get('alpha', alpha))
        beta = float(request.POST.get('beta', beta))
        delta = float(request.POST.get('delta', delta))
        gamma = float(request.POST.get('gamma', gamma))
        scenario = request.POST.get('scenario', scenario)

        # Handle validation
        if x0 < 0:
            has_errors = True
            x0_error = "x0 must be positive."
        
        if y0 < 0:
            has_errors = True
            y0_error = "y0 must be positive."

        if alpha < 0:
            has_errors = True
            alpha_error = "alpha must be positive."

        if beta < 0:
            has_errors = True
            beta_error = "beta must be positive."
        
        if delta < 0:
            has_errors = True
            delta_error = "delta must be positive."

        if gamma < 0:
            has_errors = True
            gamma_error = "gamma must be positive."

    # Run simulation
    pop_dynamics_plot = None
    phase_space_plot = None
    if not has_errors:
        t, z = run_pred_prey_simulation(x0, y0, alpha, beta, delta, gamma)

        # Population dynamics plot
        pop_dynamics_fig = generate_population_dynamics_plot(t, z)
        pop_dynamics_plot = PlotlyView(pop_dynamics_fig)
        
        # Phase space plot
        phase_space_fig = generate_phase_space_plot(z)
        phase_space_plot = PlotlyView(phase_space_fig)

    # Initialize the scenario select input
    scenario_options = [(v['name'], k) for k, v in SCENARIOS.items()]
    scenario_select = SelectInput(
        display_text='Scenario',
        name='scenario',
        multiple=False,
        options=scenario_options,
        initial=scenario,
    )

    context = {
        'initial_x0': x0,
        'initial_y0': y0,
        'initial_alpha': alpha,
        'initial_beta': beta,
        'initial_delta': delta,
        'initial_gamma': gamma,
        'x0_error': x0_error,
        'y0_error': y0_error,
        'alpha_error': alpha_error,
        'beta_error': beta_error,
        'delta_error': delta_error,
        'gamma_error': gamma_error,
        'pop_dynamics_plot': pop_dynamics_plot,
        'phase_space_plot': phase_space_plot,
        'scenario_select': scenario_select,
        'scenario_data': SCENARIOS,
    }
    return render(request, 'pred_prey/home.html', context)