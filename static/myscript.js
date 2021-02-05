//const toggleButton = document.getElementsByClassName("toggle-button")[0]
//const navBar = document.getElementsByClassName("navbar")[0]

//toggleButton.addEventListener("click", () => {
//    navBar.classList.toggle("active")
//}
//)




//   $(".navbar").toggleClass("active");
//    $(".bar").toggleClass("active");
//}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}