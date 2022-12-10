var slideIndex = 0;
var imgindex = 1;
window.onload = function() {
  showDivs(slideIndex)
}

showDivs(slideIndex)

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = Array.from(document.getElementsByClassName("mySlides"));
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "flex";  
}

function outputrange() {
  var range=document.getElementById("price");
  document.getElementById("value").innerHTML="<h3>"+range.value+"€"+"</h3>";
}

function popup() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}

function changesrc(){
    imgindex++
    a = document.getElementById("A")
    if (imgindex <= 3){
        a.src = "./src/img/tlou"+imgindex+".png"
    }else{
        imgindex=1
        a.src = "./src/img/tlou"+imgindex+".png"
    }
    
}