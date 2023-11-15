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
                    "X-CSRFToken": get_csrf_token(),
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: formJsonString,
                credentials: 'same-origin',
            }).then(response => {
                if (!response.ok) {
                    console.error('Error: ' + response.status);
                }
                return response.json();
            }).then(json => {
                console.log(json);
                // Update plots
            }).catch(
                error => console.error('Error: ' + error)
            );
        });
    });
});