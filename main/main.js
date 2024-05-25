let annee = "2024";
let nbSujets = 48;

const formater_chiffre = chiffre => chiffre > 9 ? chiffre.toString() : "0" + chiffre.toString();
const chemin = numero => `../sujets/sujets_${annee}/sujet_${numero}/sujet_${formater_chiffre(numero)}`

function sujet_py(numero) {
    return chemin(numero) + "_py.py";
}

function chemin_sujet_pdf(numero) {
    return chemin(numero) + ".pdf";
}

function correction_1(numero) {
    return chemin(numero) + "_correction_1.py";
}

function correction_2(numero) {
    return chemin(numero) + "_correction_2.py";
}

function afficherFichier(file, callback) {
    const rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status === 0) {
                const allText = rawFile.responseText;
                callback(allText);
            }
        }
    }
    rawFile.send(null);
}

function createRepl(text, id="") {
    const repl = document.createElement("py-repl");
    repl.id = id;
    repl.innerHTML = text;
    return repl
}

function chargerSujet(numero) {
    afficherFichier(sujet_py(numero), (text) => {
       const replEx1 = createRepl("# Exercice 1");
       const replEx2 = createRepl("# Exercice 2 \n\n" + text, "repl");
       document.getElementById("div-repl").replaceChildren(replEx1, replEx2)
    });
    document.getElementById("sujet_pdf").src = chemin_sujet_pdf(numero);
}

function chargerCorrection(numero) {
    const correction = document.getElementById("correction");
    correction.innerHTML = "";
    afficherFichier(correction_1(numero), (text) => {
        correction.innerHTML = text;
    });
    correction.innerHTML += "\n";

    afficherFichier(correction_2(numero), (text) => {
        correction.innerHTML += text;
    });
}

function effacerTerminal() {
    document.getElementById("terminal").children[0].innerHTML = "";
}

function montrerCorrection() {
    document.getElementById("div-correction").style.left = "50%";
}

function fermerCorrection() {
    document.getElementById("div-correction").style.left = "125%";
}

document.getElementById("effacer").onclick = effacerTerminal;
document.getElementById("montrer_correction").onclick = montrerCorrection;
document.getElementById("fermer").onclick = fermerCorrection;

function chargerSujetRandom() {
    const random = Math.floor(Math.random() * nbSujets) + 1;
    chargerSujet(random);
    chargerCorrection(random);
}

document.getElementById("next-sujet").onclick = () => {
    effacerTerminal();
    fermerCorrection();
    chargerSujetRandom();
}

function main() {
    chargerSujet(4);
    chargerCorrection(4);
}

main();


