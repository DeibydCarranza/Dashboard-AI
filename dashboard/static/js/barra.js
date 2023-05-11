document.addEventListener("DOMContentLoaded", function() {
    const body = document.querySelector('body'),
          sidebar = body.querySelector('nav'),
          toggle = body.querySelector(".toggle"),
          searchBtn = body.querySelector(".search-box"),
          modeSwitch = body.querySelector(".toggle-switch"),
          modeText = body.querySelector(".mode-text"),
          header = body.querySelector("header");
  
    // Al cargar la página, comprobar si el valor del darkmode ya está almacenado y aplicarlo si es necesario
    if (localStorage.getItem("darkmode") === "true") {
      body.classList.add("dark");
      modeText.innerText = "Light mode";
      if (header) { // Si existe el header, agregar la clase "dark"
        header.classList.add("dark");
      }
    } else {
      body.classList.remove("dark");
      modeText.innerText = "Dark mode";
      if (header) { // Si existe el header, remover la clase "dark"
        header.classList.remove("dark");
      }
    }
  
    toggle.addEventListener("click", () => {
      sidebar.classList.toggle("close");
    })
  
    searchBtn.addEventListener("click", () => {
      sidebar.classList.remove("close");
    })
  
    modeSwitch.addEventListener("click", () => {
      body.classList.toggle("dark");
  
      // Al hacer clic en el botón del modo oscuro, almacenar el valor actual en el navegador
      if (body.classList.contains("dark")) {
        localStorage.setItem("darkmode", "true");
        modeText.innerText = "Light mode";
        if (header) { // Si existe el header, agregar la clase "dark"
          header.classList.add("dark");
        }
      } else {
        localStorage.setItem("darkmode", "false");
        modeText.innerText = "Dark mode";
        if (header) { // Si existe el header, remover la clase "dark"
          header.classList.remove("dark");
        }
      }
    });
  });
  