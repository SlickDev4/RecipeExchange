function setupLoginForm() {
    const labels = document.querySelectorAll('.login-box label');
    const inputs = document.querySelectorAll('.login-box input');
    const errorlist = document.querySelectorAll('.login-box .errorlist');

    const emailLabel = labels[0];
    const passwordLabel = labels[1];

    const emailInput = inputs[2];
    const passwordInput = inputs[3];

    function updateLabelPosition(inputElement, labelElement, topWhenActive, topWhenInactive) {
        if (inputElement.value.length > 0 || inputElement === document.activeElement) {
            labelElement.style.top = topWhenActive;
        } else {
            labelElement.style.top = topWhenInactive;
        }
    }

    function handleErrorMessage(errorlist, emailInput) {
        if (errorlist.length > 0 && errorlist[0].children.length > 0) {
            let errors = errorlist[0].textContent.trim();

            emailInput.style.color = 'red';
            emailInput.value = errors;
            errorlist[0].innerHTML = '';
        }
    }

    function clearEmailInput(emailInput) {
        if (emailInput.value === 'Wrong email or password.') {
            emailInput.value = '';
            emailInput.style.color = 'whitesmoke';
        }
    }

    setInterval(() => {
        updateLabelPosition(emailInput, emailLabel, '19%', '27%');
        updateLabelPosition(passwordInput, passwordLabel, '44%', '52%');
    }, 100);

    setInterval(() => {
        handleErrorMessage(errorlist, emailInput);
    }, 100);

    emailInput.addEventListener('focus', function() {
        clearEmailInput(emailInput);
    });
}

setupLoginForm();
