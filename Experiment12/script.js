document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('hello').style.color = 'blue';

  let counter = 0;
  const counterButton = document.getElementById("counterButton");
  const counterDisplay = document.getElementById("counterDisplay");

  counterButton.addEventListener("click", function() {
    counter++;
    counterDisplay.textContent = counter;
  });
});
