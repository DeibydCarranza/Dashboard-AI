// boton.js

function addClickEventToButton() {
    var id_str = "toggle-button-{index}";
  
    var button = document.getElementById(id_str);
    if (button) {
      button.addEventListener("click", function() {
        var table = document.getElementById("table-{index}");
        if (table.style.display === "none") {
          table.style.display = "block";
        } else {
          table.style.display = "none";
        }
      });
    } else {
      setTimeout(addClickEventToButton, 100); // Intenta nuevamente después de 100 milisegundos
    }
  }
  
  addClickEventToButton();
  
  