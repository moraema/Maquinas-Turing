async function ejecutarMaquina(event) {
    event.preventDefault();
    const cinta = document.querySelector('input[name="cinta"]').value;
    const resultadoDiv = document.getElementById("resultado");

    resultadoDiv.classList.add('mostrar');
    resultadoDiv.innerHTML = '<span class="mensaje-validando">Validando cadena...</span>';
    
    
    const response = await fetch("http://localhost:5001/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({ cinta })
    });

    
    const resultado = await response.text();
    setTimeout(() => {
        resultadoDiv.innerHTML = `
            <strong>Posibles vulnerabilidades:</strong><br>
            <span class="resultado-info">${resultado}</span>
        `;
    }, 1000);
    
}



function abrirModal(id) {
    document.getElementById(id).style.display = 'block';
}

function cerrarModal(id) {
    document.getElementById(id).style.display = 'none';
}

// Cierra el modal al hacer clic fuera del contenido
window.onclick = function(event) {
    const modals = document.getElementsByClassName('modal');
    for (let modal of modals) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

window.onclick = function(event) {
    if (event.target === document.getElementById("modalEjemplos")) {
        cerrarModal();
    }
}
