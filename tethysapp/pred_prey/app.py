from tethys_sdk.base import TethysAppBase


class PredPrey(TethysAppBase):
    """
    Tethys app class for Predator Prey.
    """

    name = 'Predator Prey'
    description = 'A calculator-style that demonstrates the Predator-Prey model.'
    package = 'pred_prey'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'pred-prey'
    color = '#8e44ad'
    tags = ''
    enable_feedback = False
    feedback_emails = []