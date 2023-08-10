function handleImageFields() {
    window.onload = function() {
        const div = document.getElementsByClassName('rmv-img')[0];

        const title = div.firstChild;
        const input = div.lastChild;

        div.innerHTML = '';

        div.appendChild(title);
        div.appendChild(input);
    };
}

handleImageFields();
