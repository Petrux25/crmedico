//Arrays de Datos
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

diassemana = ["D", "L", "K", "M", "J", "V", "S"];

lasemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Vierves", "Sábado", "Domingo"]

window.onload = function() {
    //fehca actual
    hoy = new Date();
    diasemhoy = hoy.getDay(); //objeto fecha actual
    diahoy = hoy.getDate(); //dia mes actual
    meshoy = hoy.getMonth(); //mes actual
    annohoy = hoy.getFullYear(); //año actual

    // Elementos del DOM: en cabecera de calendario
    titulo = document.getElementById("datetitle"); //cabecera del calendario
    m_ant = document.getElementById("m_anterior"); //mes anterior
    m_pos = document.getElementById("m_posterior"); //mes posterior
    w_ant = document.getElementById("w_anterior"); //semana anterior
    w_pos = document.getElementById("w_posterior"); //semana posterior

    // Elementos del DOM en primera fila
    dias = document.getElementById("dias");

    // Operaciones para determinar semana
    number_weeks = weeks_in_month();
    w_actual = Math.ceil(diahoy / 7)

    // Pie de calendario
    pie = document.getElementById("fechaactual");
    pie.innerHTML += " " + lasemana[diasemhoy] + ", " + diahoy + " de " + meses[meshoy] + " del " + annohoy + "-- SEMANA: " + w_actual;



    // Definir elementos inciales:
    mes_actual = meshoy; //mes principal
    anno_actual = annohoy; //año principal

    cabecera_meses();
    cabecera_semanas();
    primeralinea();

}

// primera línea de la tabla: días de la semana
function primeralinea() {
    for (i = 0; i < 7; i++) {
        celda0 = dias.getElementsByTagName("th")[i];
        celda0.innerHTML = diassemana[i] + "-"; //Falataría agregar la fecha (el día)
    }
}

function cabecera_meses() {
    titulo.innerHTML = meses[mes_actual] + " del " + anno_actual;
    mesant = mes_actual - 1; //mes anterior
    mespos = mes_actual + 1; //mes posterior
    if (mesant < 0) {
        mesant = 11;
    }
    if (mespos > 11) {
        mespos = 0;
    }
    m_ant.innerHTML = meses[mesant];
    m_pos.innerHTML = meses[mespos];
}

function cabecera_semanas() {
    semant = w_actual - 1; //Semana anterior
    sempos = w_actual + 1; //Semana posterior
    mes = mes_actual; //copia del mes actual

    if (semant < 1) {
        if (mes - 1 < 0) {
            mes = 12
        }
        semant = weeks_in_month(mes);
    }
    if (sempos > number_weeks) {
        // if (mes + 1 > 12) {
        //     mes = 1;
        // }
        // sempos = weeks_in_month(mes);
        sempos = 1;
    }
    w_ant.innerHTML = semant;
    w_pos.innerHTML = sempos;
}

// Cantidad de "semanas" en un determinado mes
function weeks_in_month() {
    if ((daysInMonth() / 7) -
        (Math.floor(daysInMonth() / 7)) > 0) {
        return Math.floor(daysInMonth() / 7) + 1;
    }
    return Math.floor(daysInMonth() / 7)
}

// Cantidad de días en un determinado mes
function daysInMonth() {
    return new Date(hoy.getFullYear(), hoy.getMonth() + 1, 0).getDate();
}