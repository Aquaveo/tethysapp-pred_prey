window.addEventListener('load', function(event) {
    let form_controls = document.querySelectorAll('.form-control');
    form_controls.forEach(fc => {
        fc.addEventListener('change', function(event) {
            console.log(event.target.value);
            // Get form values and convert to json
            const formData = new FormData(document.querySelector('#parameters-form'));
            const formJson = Object.fromEntries(formData.entries());
            console.log(formJson);
            
            // Submit fetch request to run simulation
            const formJsonString = JSON.stringify(formJson);
            fetch('/apps/pred-prey/run-simulation/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: formJsonString,
            }).then(response => {
                if (response.ok) {
                    return response.json();
                }
                else {
                    console.error('Error: ' + response.status);
                    console.error(response.body);
                }
            }).then(data => {
                console.log(data);
            });

            // Update plots
        });
    });
});