const popup = document.querySelector('.newsletter-popup-content');
const close = document.querySelector('.close');

window.onload = function(){
    setTimeout(function(){
      popup.style.display = "block"

    }, 2000 )
}

close.addEventListener('click', () => {
    popup.style.display = "none";
})


// window.addEventListener("load", function(){
//   setTimeout(
//       function open(event){
//           document.querySelector(".newsletter-popup-container").style.display = "block";
//       },
//       1000
//   )
// });


// document.querySelector("#close").addEventListener("click", function(){
//   document.querySelector(".popup").style.display = "none";
// });