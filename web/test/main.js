
const button = document.getElementById('consoleButton');
button.addEventListener('click', () => {
    console.log('Clicked!');
});

const input = document.getElementById('textInput');
input.addEventListener('input', (event) => {
    console.log(`Texte saisi : ${event.target.value}`);
});