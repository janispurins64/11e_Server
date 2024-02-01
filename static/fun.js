async function sendDataToServer() {
    const url = 'http://127.0.0.1:5000/dts';  // Aizstājiet ar savu servera adresi
    const dataToSend = { vards: 'Juris', uzvards: "Vētra" };  // Jūsu nosūtāmie dati

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSend),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Izsauciet funkciju, kad lapas ielādējas vai pēc kāda notikuma
//sendDataToServer();









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

