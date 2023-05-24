/*  Manejo de evento en sección de carga CSV -> tipo archivo */
document.querySelector('.box-upload').addEventListener('click', function() {
    document.querySelector('input[type="file"]').click();
  });

/* Generando petición y respuesta al archivo cargado desde /upload_csv */
function submitForm() {
    var form = document.getElementById('csv-form');
    var formData = new FormData(form);
    var fileInput = document.querySelector('input[type="file"]');
    var selectedFile = fileInput.files[0];
    formData.append('uploaded_file', selectedFile);


    var peticion = new XMLHttpRequest();
    peticion.open('POST', '/upload_csv', true);

    peticion.onload = function() {
        if (peticion.status === 200) {
        console.log(peticion.responseText);
        document.getElementById('render-container').style.display = 'block';
        } else {
        console.log('Error:', peticion.status);
        }
    };
    
    peticion.onerror = function() {
        console.log('Request Error:', peticion.status); 
    };
    peticion.send(formData);
}
  