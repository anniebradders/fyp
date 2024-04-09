document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('percentage_slider');
    const output = document.getElementById('percentage_value');
    output.textContent = slider.value; // Display the default slider value

    slider.oninput = function() {
        output.textContent = this.value;
    };
});