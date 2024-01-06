// Ejemplo 1
let numero = 5;
let texto = "Welcome to osu!";
let esVerdadero = true;

// Ejemplo 2
let suma = 10 + 5;
let concatenacion = "Hola" + " " + "mundo";

// Ejemplo 3
if (condicion) {
    console.log("La condicion es verdadera");
} else {
    console.log("La condicion es falsa");
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Ejemplo 4
function saludar(nombre) {
    return "Hola, " + nombre + "!";
}

let saludo = saludar("William");


// Ejemplo 5
let persona = {
    nombre: "William",
    edad: 18,
    decirHola: function() {
        console.log("Hola, soy " + this.nombre);
    }
};

// Ejemplo 6
let numeros = [1, 2, 3, 4, 5, 7, 2, 7];

// Ejemplo de la funcion fetch
fetch('https://osu.ppy.sh/home')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
