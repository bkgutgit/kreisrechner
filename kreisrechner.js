/* beispiel_ls3_06.js - Kreisrechner mit HTML, W3.CSS und Javascript
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  27.09.2022, 22.10.2022
    */


function kreisdatenBerechnen() {
    let radius, umfang, flaeche;

    radius = radiusEinlesen();
    if(radius < 0){
        alert("Der Radius darf nicht negativ sein!");
        return;
    }
    umfang = umfangBerechnen(radius);
    flaeche = flaecheBerechnen(radius);
    ergebnisseAnzeigen(umfang, flaeche);

}


function radiusEinlesen() {
    const radius = Number(document.getElementById("id1").value)
    return radius;
}


function umfangBerechnen(radius) {
    let umfang;
    umfang = 2 * Math.PI * radius;
    umfang = runden(umfang);
    return umfang;
}


function flaecheBerechnen(radius) {
    let flaeche;
    flaeche = Math.PI * Math.pow(radius, 2);
    flaeche = runden(flaeche);
    return flaeche;
}


function ergebnisseAnzeigen(umfang, flaeche) {
    document.getElementById("id2").innerHTML = umfang;
    document.getElementById("id3").innerHTML = flaeche;
    return;
}


function runden(zahl) {
    zahl = Math.round(zahl * 100) / 100;
    return zahl;
}


function loeschen() {
    document.getElementById("id2").innerHTML = "";
    document.getElementById("id3").innerHTML = "";
    return;
}