console.log('main.js');

function myFunction() {
    const copyText = document.getElementById("long_url");
    navigator.clipboard.writeText(copyText.innerText);

    const button = document.getElementById("copyBtn");
    button.innerText = "Copied!";
}