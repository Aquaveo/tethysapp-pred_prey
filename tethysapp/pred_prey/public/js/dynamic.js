window.addEventListener('load', function(event) {
    let form_controls = document.querySelectorAll('.form-control');
    form_controls.forEach(fc => {
        fc.addEventListener('change', function(event) {
            // Get form values and convert to json
            const formData = new FormData(document.querySelector('#parameters-form'));
            const formJson = Object.fromEntries(formData.entries());
            console.log(formJson);
            
            // Submit fetch request to run simulation
            const formJsonString = JSON.stringify(formJson);
            fetch('/apps/pred-prey/run-simulation/', {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    "X-CSRFToken": get_csrf_token(),
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: formJsonString,
            }).then(response => {
                if (!response.ok) {
                    console.error('Error: ' + response.status);
                    return;
                }
                return response.json();
            }).then(json => {
                if (!json.success) {
                    console.error('Error: ' + json.error);
                    return;
                }

                // Update plots
                let popDynamicsPlot = JSON.parse(json.pop_dynamics_plot);
                let popDynamicsPlotDiv = document.querySelector('#population-dynamics-container .plotly-graph-div');
                Plotly.react(popDynamicsPlotDiv, popDynamicsPlot.data, popDynamicsPlot.layout);
                let phaseSpacePlot = JSON.parse(json.phase_space_plot);
                let phaseSpacePlotDiv = document.querySelector('#phase-space-container .plotly-graph-div');
                Plotly.react(phaseSpacePlotDiv, phaseSpacePlot.data, phaseSpacePlot.layout);
            }).catch(
                error => console.error('Error: ' + error)
            );
        });
    });
});