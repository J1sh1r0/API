// Importa las funciones del módulo mathOperations
import { sumar, restar, multiplicar, dividir } from './mathOperations.js';

// Uso de las funciones
console.log("Suma: ", sumar(5, 3)); // Suma: 8
console.log("Resta: ", restar(5, 3)); // Resta: 2
console.log("Multiplicación: ", multiplicar(5, 3)); // Multiplicación: 15

// Manejo de la división, con captura de errores si el divisor es 0
try {
    console.log("División: ", dividir(10, 2)); // División: 5
    console.log("División: ", dividir(10, 0)); // Error: El denominador no puede ser 0.
} catch (error) {
    console.error(error.message); // Muestra el mensaje de error
}
