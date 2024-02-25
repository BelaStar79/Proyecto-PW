document.getElementById("btn__iniciar-sesion").addEventListener('click', iniciarSesion),
document.getElementById("btn__registrarse").addEventListener('click', register);
window.addEventListener("resize", anchoPagina);


//Declaración de variables
var contenedor_login_register = document.querySelector(".contenedor__login__register");
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var caja_trasera_login = document.querySelector(".caja__trasera-login");
var caja_trasera_register = document.querySelector(".caja__trasera-register");


function anchoPagina() {

    if(window.innerWidth > 850){
        caja_trasera_login.style.display = "block";
        caja_trasera_register.style.display = "block";
    }else{
        caja_trasera_register.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display = "block";
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
    }

}


function iniciarSesion() {

    if(window.innerWidth > 850){
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "10px";
        formulario_login.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.opacity = "0";
    }else{
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "block";
        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "none";
    }

}


function register() {
    
    if(window.innerWidth > 850){
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "410px";
        formulario_login.style.display = "none";
        caja_trasera_register.style.opacity = "0";
        caja_trasera_login.style.opacity = "1";
    }else{
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "none";
        caja_trasera_register.style.display = "none";
        caja_trasera_login.style.display = "block";
        caja_trasera_login.style.opacity = "1";
    }
    
}


// inicio de la validacion del formulario de login
function validarFormularioLogin() {

    var contrasena = document.getElementsByName('contrasena')[0].value;
    var correo = document.getElementsByName('correo')[0].value;
  
    if (contrasena === '' || correo === '') {
        alert('Por favor, completa todos los campos.');
        return false; 
    }
  
    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
    if (!correoRegex.test(correo)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false; 
    }
  
    return true;
}
// fin de la validacion del formulario de login 


// inicio de la validacion del formulario de register
function validarFormularioRegister() {

    var nombre = document.getElementsByName('nombre')[0].value;
    var correo = document.getElementsByName('correo')[0].value;
    var usuario = document.getElementsByName('usuario')[0].value;
    var contrasena = document.getElementsByName('contrasena')[0].value;

    if (nombre === '' || correo === '' || usuario === '' || contrasena === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }

    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!correoRegex.test(correo)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false;
    }

    if (contrasena.length < 8) {
        alert('La contraseña debe tener al menos 8 caracteres.');
        return false;
    }

    return true;
}
  // fin de la validacion del formulario de register 
  