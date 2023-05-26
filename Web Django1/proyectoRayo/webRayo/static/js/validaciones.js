function validar(){
    validarEdad();
    validarContraseña();
    return false;
}





function validarContraseña(){
    let Pass1=document.getElementById("txtPass1").value;
    let Pass2=document.getElementById("txtPass2").value;
    if (Pass1==Pass2) {
        alert('OK')
    } else {
        Swal.fire('contraseñas incorrectas');
        return false;

    }
}
function validarEdad(){
    var fecha=document.getElementById("datFecha").value;
    var fechaSistema=new Date();
    console.log('Fecha Recuperada:'+fecha);
    console.log('fecha sistema:' +fechaSistema);

    var annio=fecha.slice(0,4);
    var mes=fecha.slice(5,7);
    var dia=fecha.slice(8,9);

    console.log('Dia: '+dia);
    console.log('Mes: '+mes);
    console.log('Año: '+annio);
    var FechaUsuario=new Date(annio,(mes-1),dia);
    if (FechaUsuario>=fechaSistema) {
        alert('edad incorrecta')
    } else {
        alert('OK')
        return true;
    }
}