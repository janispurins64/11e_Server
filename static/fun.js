
async function lasiPersonas() {
    const atbilde = await fetch('http://127.0.0.1:5000/personas');
    const datuObjekts = await atbilde.json();
    console.log(datuObjekts);
    console.log("Bla Bla ----------------------")
    raadiPersonas(datuObjekts);
}

// Ieliekam jaununierakstu izvēles sarakstā
const raadiPersonas = (dati) => {
    const personasUL = document.getElementById("persona1");
    // novaacam ieprieksheejo saturu
   while (personasUL.firstChild) {
       personasUL.firstChild.remove();
   }
    // ieliekam jaunu saturu
	console.log(personasUL);
   for (let rinda of dati["personas"]) {
		var option = new Option();
		option.text = rinda;
		option.value = rinda;
		personasUL.appendChild(option);
   }
  console.log(dati);
  }
//raadiPersonas(dati);

