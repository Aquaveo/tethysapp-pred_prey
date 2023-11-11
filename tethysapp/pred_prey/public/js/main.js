window.addEventListener('load', function(event) {
    // Trigger window resize to fix the plot width issue
    window.dispatchEvent(new Event('resize'));

    // Load data
    const d = document.querySelector('#data');
    const scenario_data = JSON.parse(d.dataset.scenarios);

    // jQuery Example: Bind event to the scenario select
    $('#scenario').on('change', function() {
        let selected_scenario = $('#scenario').val();
        let selected_scenario_data = scenario_data[selected_scenario];

        // update form fields
        $('#alpha-input').val(selected_scenario_data.alpha);
        $('#beta-input').val(selected_scenario_data.beta);
        $('#delta-input').val(selected_scenario_data.delta);
        $('#gamma-input').val(selected_scenario_data.gamma);
    });
});