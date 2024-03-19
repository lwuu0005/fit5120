document.addEventListener('DOMContentLoaded', function () {
    var paginationButtons = document.querySelectorAll('#pagination button');
    var slider = document.getElementById('slider');
    var sliderInner = document.querySelector('.slider-inner');

    function updateSlider(slideIndex) {
        sliderInner.style.opacity = '0';

        // Use setTimeout to wait for the fade-out transition to complete
        setTimeout(function () {
            // Set the data-slide attribute to the new slide
            slider.setAttribute('data-slide', slideIndex);

            // Update active class for pagination buttons
            paginationButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });
            document.querySelector('#pagination button[data-slide="' + slideIndex + '"]').classList.add('active');

            // Update slide title and status
            var slideTitle = document.querySelector('span[data-slide-title="' + slideIndex + '"]').textContent;
            var slideStatus = document.querySelector('span[data-slide-status="' + slideIndex + '"]').textContent;
            document.getElementById('slide-title').innerHTML = slideTitle;
            document.getElementById('slide-status').textContent = slideStatus;

            // Finally, make the new slide fully opaque
            sliderInner.style.opacity = '1';
        }, 1000); // This timeout should match the duration of the fade-out transition
    }

    // Update slider on button click
    paginationButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            updateSlider(this.getAttribute('data-slide'));
        });
    });

    // Update the slider for the first slide on page load
    updateSlider('0');
});
