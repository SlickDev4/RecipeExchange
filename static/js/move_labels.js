const labels = document.querySelectorAll('.login-box label');
const inputs = document.querySelectorAll('.login-box input');
const errorlist = document.querySelectorAll(".login-box .errorlist");

let email_label = labels[0];
let password_label = labels[1];

let email_input = inputs[2];
let password_input = inputs[3];


function labelPos(email_input, email_label, password_input, password_label) {
    
    if (email_input.value.length > 0 || email_input === document.activeElement) {
        email_label.style.top = "19%";
    } else {
        email_label.style.top = "27%";
    }

    if (password_input.value.length > 0 || password_input === document.activeElement) {
        password_label.style.top = "44%";
    } else {
        password_label.style.top = "52%";
    }
}


function checkErrorMessages(errorlist, email_input) {
    if (errorlist.length > 0 && errorlist[0].children.length > 0) {
        let errors = errorlist[0].textContent.replace(/^\s+|\s+$/g, '');

        email_input.style.color = "red";
        email_input.value = errors;
        errorlist[0].innerHTML = "";
    }
}


function clearInput(email_input) {
    if (email_input.value === "Wrong email or password.") {
        email_input.value = "";
        email_input.style.color = "whitesmoke";
    }
}

setInterval(() => {labelPos(email_input, email_label, password_input, password_label)}, 100);
setInterval(() => {checkErrorMessages(errorlist, email_input)}, 100);

email_input.addEventListener("focus", function() {clearInput(email_input)})

