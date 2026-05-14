const boton = document.getElementById('btnCambiar');
const parrafo = document.getElementById('mensaje');

// Evento: Al hacer clic en el botón
boton.addEventListener('click', () => {
    parrafo.textContent = "¡Día fantástico para Francisco de Paula! (Ref: F.P.P.F)";
    
    // Cambiamos el color a naranja
    parrafo.style.color = "orange";
});

// Extra: Al pasar el ratón por encima (mouseenter)
boton.addEventListener('mouseenter', () => {
    // Sustituye [Tu Apellido]
    boton.textContent = "¡Púlsame, Pulido!";
});