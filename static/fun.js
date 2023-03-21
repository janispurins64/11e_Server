
async function lasiPersonas() {
    const atbilde = await fetch('http://127.0.0.1:5000/persona');
    const datuObjekts = await atbilde.json();
    console.log(datuObjekts);
    console.log("Bla Bla ----------------------")
    raadiPersonas(datuObjekts);
}
const dati = {"personas":["Juris Ozols","Māris Liepiņš", "Guna Apse"]}

// Ieliekam jaununierakstu izvēles sarakstā
const raadiPersonas = (dati) => {
    const personasUL = document.querySelector(".persona1");
    // novaacam ieprieksheejo saturu
   // while (personasUL.firstChild) {
   //     personasUL.firstChild.remove();
   // }
    // ieliekam jaunu saturu
   for (let rinda of dati["personas"]) {
      personaN = izveidoJaunuPers(rinda);
      personasUL.appendChild(personaN);
   }
  console.log(dati);
  }

const izveidoJaunuPers = (zinja) => { 
    let newLI = document.createElement("option");
    newLI.setAttribute("name",zinja);
    newLI.innerHTML = zinja;
    return newLI;
  }
const laikaParbaude = () =>{
    console.log("Kārtējais tikšķis");
}
raadiPersonas(dati);
setTimeout(laikaParbaude,1000);

