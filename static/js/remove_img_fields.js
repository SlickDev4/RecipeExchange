window.onload = function() {
    const div = document.getElementsByClassName("test")[0];

    const title = div.firstChild;
    const input = div.lastChild;

    div.innerHTML = "";

    div.appendChild(title);
    div.appendChild(input);
    
};