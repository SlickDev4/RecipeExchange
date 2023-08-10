function setupRecipeDetailsButtons() {
    const buttonElements = document.getElementsByClassName('js-button');
    const spanElements = document.getElementsByClassName('js-span');
    const liked = document.getElementById('js-liked');
    const authorOrUser = document.getElementById('js-author');

    const buttons = [];
    const icons = [];
    let index = 0;

    function pushElements() {
        for (let i = 0; i < buttonElements.length; i++) {
            icons.push(buttonElements[i]);
            buttons.push(spanElements[i]);
        }

        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.transition = '0.5s ease';
            icons[i].style.transition = '0.5s ease';
        }
    }

    function addEvents() {
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener('mouseenter', function(event) {
                buttons[i].style.color = 'rgb(1, 183, 255)';
                icons[i].style.color = 'rgb(1, 183, 255)';
            });

            icons[i].addEventListener('mouseenter', function(event) {
                buttons[i].style.color = 'rgb(1, 183, 255)';
                icons[i].style.color = 'rgb(1, 183, 255)';
            });

            buttons[i].addEventListener('mouseleave', function(event) {
                buttons[i].style.color = 'whitesmoke';
                checkHovers(i, icons[i]);
            });

            icons[i].addEventListener('mouseleave', function(event) {
                buttons[i].style.color = 'whitesmoke';
                checkHovers(i, icons[i]);
            });
        }
    }

    function checkAuthorOrUser() {
        if (authorOrUser.textContent === 'True') {
            index = 2;
        } else {
            index = 0;
        }
    }

    function checkLiked() {
        if (liked.textContent === 'True') {
            icons[index].style.color = 'rgb(1, 183, 255)';
            buttons[index].textContent = 'Dislike';
        } else {
            icons[index].style.color = 'whitesmoke';
            buttons[index].textContent = 'Like';
        }
    }

    function checkHovers(i, element) {
        if (i === index) {
            if (liked.textContent === 'False') {
                element.style.color = 'whitesmoke';
            } else {
                element.style.color = 'rgb(1, 183, 255)';
            }
        } else {
            element.style.color = 'whitesmoke';
        }
    }

    pushElements();
    addEvents();
    checkAuthorOrUser();
    checkLiked();
}

setupRecipeDetailsButtons();
