window.addEventListener('load', function(event) {
    // Trigger window resize to fix the plot width issue
    window.dispatchEvent(new Event('resize'));
});