const button = document.getElementsByClassName('js-button')[0];
const icon = document.getElementsByClassName('js-span')[0];

button.style.transition = '0.5s ease';
icon.style.transition = '0.5s ease';

button.addEventListener('mouseenter', function(event) {
    button.style.color = 'rgb(1, 183, 255)';
    icon.style.color = 'rgb(1, 183, 255)';
});

button.addEventListener('mouseleave', function(event) {
    button.style.color = 'whitesmoke';
    icon.style.color = 'whitesmoke';
});
