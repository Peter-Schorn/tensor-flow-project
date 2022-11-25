const button = document.getElementById("search-categories");

button.addEventListener("click", () => {
    console.log("clicked");
});

const searchField = document.querySelector(".search-field");
searchField.addEventListener('input', (event) => {
    console.log(`Input: ${event}`);
});
