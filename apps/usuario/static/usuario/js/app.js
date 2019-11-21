/* function validarFormulario(){

    var registrarse= true;
    
    var valNombre= /^[a-zA-Z\s]+$/;
    var valApaterno= /^[a-zA-Z\s]+$/;
    var valAmaterno= /^[a-zA-Z\s]+$/;
    var valRut= /[0-9]{9}$/;
    var valNbip= /[0-9]{7}$/;
    
    var nombre = document.getElementById("nombre");
    var apaterno = document.getElementById("apaterno");
    var amaterno = document.getElementById("amaterno");
    var rut = document.getElementById("rut");
    var nbip = document.getElementById("nbip");
    var formulario = document.getElementById("formulario");
  
    if(!nombre.value){
        alert("Ingrese su nombre.")
        nombre.focus();
    }
    else if(!valNombre.exec(nombre.value))
    {
    alert("Este campo sólo acepta letras.");
    registrarse=false;
    nombre.focus();
    }
    else if(!apaterno.value){
        alert("Ingrese su apellido paterno.")
        apaterno.focus();
    }
    else if(!valApaterno.exec(apaterno.value))
    {
    alert("Este campo sólo acepta letras.");
    registrarse=false;
    apaterno.focus(); 
    }
    else if(!amaterno.value){
        alert("Ingrese su apellido materno.")
        amaterno.focus();
    }
    else if(!valAmaterno.exec(amaterno.value))
    {
    alert("Este campo sólo acepta letras.");
    registrarse=false;
    amaterno.focus(); 
    }    
    else if(!rut.value){
        alert("Ingrese su rut sin guión.")
        rut.focus(); 
    }
    else if(!valRut.exec(rut.value))
    {
    alert("Este campo debe tener 9 dígitos como mínimo.");
    registrarse=false;
    rut.focus(); 
    }
    else if(!nbip.value){
        alert("Ingrese su numero de bip.")
        nbip.focus();
    }
    else if(!valNbip.exec(nbip.value))
    {
    alert("Este campo debe tener 7 dígitos como mínimo.");
    registrarse=false;
    nbip.focus(); 
    }
    else if(registrarse){
        if(confirm('¿Está seguro de que todos los datos son correctos?'))
        {
        window.location="resultado.html";
        document.formulario.submit();
        }
        else
        {
         return false;
        } 
       
      }


    
}
window.onload= function(){
    var Botonregistrarse = document.getElementById("registrarse");
    Botonregistrarse.onclick=this.validarFormulario;
    
} */