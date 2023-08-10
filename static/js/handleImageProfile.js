function handleImageProfile() {
    window.onload = function() {
        const div = document.getElementsByClassName('data')[0];
        const input = div.lastChild;

        div.innerHTML = '';
        div.appendChild(input);
    };
}

handleImageProfile();
