const toggleModal = () => {
    document.querySelector(".modal")
    .classList.toggle("modal-hidden");
};

const changeBgDark = () => {
    document.querySelector("body").style.background = "#000000";
};    
    
const changeBgLight = () => {
    document.querySelector("body").style.background = "#F1F1F1";
};   

document.querySelector("#show-modal")
    .addEventListener("click", toggleModal);

document.querySelector("#show-modal")
    .addEventListener("click", changeBgDark);   

document.querySelector("#learn-more")
    .addEventListener("submit", (event) => {
        event.preventDefault();
        toggleModal();
    });

document.querySelector("#learn-more")
    .addEventListener("submit", (event) => {
        event.preventDefault();
        changeBgLight();
    });

document.querySelector(".modal-close-bar span")
    .addEventListener("click", toggleModal);

document.querySelector(".modal-close-bar span")
    .addEventListener("click", changeBgLight);
