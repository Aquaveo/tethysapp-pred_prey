window.addEventListener('load', function(event) {
    let form_controls = document.querySelectorAll('.form-control');
    form_controls.forEach(fc => {
        fc.addEventListener('change', function(event) {
            console.log(event.target.value);
            // Get form values

            // Submit fetch request to run simulation

            // Update plots
        });
    });
});