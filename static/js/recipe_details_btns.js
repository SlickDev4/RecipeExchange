const button_elements = document.getElementsByClassName('js-button');
const span_elements = document.getElementsByClassName('js-span');
const liked = document.getElementById('js-liked')
const author_or_user = document.getElementById('js-author')

let buttons = [];
let icons = [];
let index = 0;

function push_elements () {
    for (let i=0; i < button_elements.length; i++) {
        icons.push(button_elements[i]);
        buttons.push(span_elements[i]);
    }
    
    for (let i=0; i < buttons.length; i++) {
        buttons[i].style.transition = '0.5s ease';
        icons[i].style.transition = '0.5s ease';
    }
}

function add_events () {
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
            check_hovers(i, icons[i]);
        });
    
        icons[i].addEventListener('mouseleave', function(event) {
            buttons[i].style.color = 'whitesmoke';
            check_hovers(i, icons[i]);
        });
    }
}

function check_author_or_user() {
    if (author_or_user.textContent === "True") {
        index = 2;
    } else {
        index = 0;
    }
}

function check_liked () {
    if (liked.textContent === "True") {
        icons[index].style.color = 'rgb(1, 183, 255)';
        buttons[index].textContent = "Dislike"
    } else {
        icons[index].style.color = 'whitesmoke'
        buttons[index].textContent = "Like"
    }
}

function check_hovers(i, element) {
    if (i === 2) {
        if (liked.textContent === "False") {
            element.style.color = 'whitesmoke';
        } else {
            element.style.color = 'rgb(1, 183, 255)';
        }
    } else {
        element.style.color = 'whitesmoke';
    }
}

push_elements();
add_events();
check_author_or_user();
check_liked(index);
