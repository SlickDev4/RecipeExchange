function setupRecipeCommentButton() {
    const button = document.getElementsByClassName('js-button')[0];
    const icon = document.getElementsByClassName('js-span')[0];

    function applyColorOnMouseEnter() {
        button.style.color = 'rgb(1, 183, 255)';
        icon.style.color = 'rgb(1, 183, 255)';
    }

    function restoreColorOnMouseLeave() {
        button.style.color = 'whitesmoke';
        icon.style.color = 'whitesmoke';
    }

    button.style.transition = '0.5s ease';
    icon.style.transition = '0.5s ease';

    button.addEventListener('mouseenter', applyColorOnMouseEnter);
    button.addEventListener('mouseleave', restoreColorOnMouseLeave);
}

setupRecipeCommentButton();